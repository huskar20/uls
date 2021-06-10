#!/usr/bin/env python3

# Copyright 2021 Akamai Technologies, Inc. All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys
import select
import signal
import threading

# ULS specific modules
import modules.aka_log as aka_log
import modules.UlsArgsParser as aka_parser
import modules.UlsOutput as UlsOutput
import modules.UlsInputCli as UlsInputCli
import config.global_config as uls_config
import modules.UlsMonitoring as UlsMonitoring

stopEvent = threading.Event()


def sigterm_handler(signum, frame):
    """
    Upon SIGTERM, we signal any other pending activities
    to stop right away
    """
    aka_log.log.debug(f"SIGTERM ({signum}) detected, setting stopEvent")
    stopEvent.set()


def control_break_handler():
    """
    Upon CTRL + C, we signal any other pending activities
    to stop right away
    """
    aka_log.log.debug("Control+C detected, setting stopEvent")
    stopEvent.set()


def main():

    signal.signal(signal.SIGTERM, sigterm_handler)

    # Load the Argument / ENV Var handler
    uls_args = aka_parser.init()
    if uls_args.version:
        UlsInputCli.uls_version()

    # Load the LOG system
    aka_log.init(uls_args.loglevel, uls_config.__tool_name_short__)

    # Create instances for Input and Output stream handler
    my_monitor = UlsMonitoring.UlsMonitoring(stopEvent, uls_args.input, uls_args.feed, uls_args.output)
    my_monitor.start()
    my_output = UlsOutput.UlsOutput()
    my_input = UlsInputCli.UlsInputCli()

    # Now let's handle the data and send input to output
    while not stopEvent.is_set():
        try:
            # (Re)Connect the input handler
            my_input.proc_create(product=uls_args.input,
                                 feed=uls_args.feed,
                                 cliformat=uls_args.cliformat,
                                 credentials_file=uls_args.credentials_file,
                                 credentials_file_section=uls_args.credentials_file_section,
                                 rawcmd=uls_args.rawcmd)

            input_poll = select.poll()
            input_poll.register(my_input.proc_output)
            my_input.check_proc()

            # (RE)Connect the output handler
            my_output.connect(output_type=uls_args.output,
                              host=uls_args.host,
                              port=uls_args.port,
                              http_out_format=uls_args.httpformat,
                              http_out_auth_header=uls_args.httpauthheader,
                              http_url=uls_args.httpurl,
                              http_insecure=uls_args.httpinsecure)

            if input_poll.poll(10):
                data = my_input.proc_output.readline().strip('\n').strip('\r')
                if data:
                    aka_log.log.debug(f"DATA: {data + uls_config.output_line_breaker}")
                    my_monitor.increase_message_count()
                    my_output.send_data(data + uls_config.output_line_breaker)
        except KeyboardInterrupt:
            control_break_handler()

    my_output.tear_down()

    if stopEvent.is_set():
        sys.exit(100)


if __name__ == "__main__":
    main()

# EOF
