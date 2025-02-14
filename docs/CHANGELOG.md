# Version History
## v1.3.3
|||
|---|---|
|Date|2022-02-28
|Kind| Bugfix release
|Author|mschiess@akamai.com
- **Bugfix**
  - Adopted to new MFA CLI Version (only single feed "EVENT" available anymore)
  - Amended new dates to the file headers
  - Added volume to dockerfile as data storage for "autoresume"

## v1.3.4
|||
|---|---|
|Date|2022-03-08
|Kind| Bugfix release
|Author|mschiess@akamai.comm adrocho@akamai.com
- **Minor improvements**
  - Added QRADAR log source type definitions (thx to bitonio)
  - Added SUMO Logic (thx to huskar20 for the contribution)
  - bumped CLI-MFA to v0.0.9
  - added resources, nodeSelector, tolerations and affinity to the helm values.yaml / template


## v1.3.3
|||
|---|---|
|Date|2022-02-28
|Kind| Bugfix release
|Author|mschiess@akamai.com
- **Bugfix**
  - Adopted to new MFA CLI Version (only single feed "EVENT" available anymore)
  - Amended new dates to the file headers
  - Added volume to dockerfile as data storage for "autoresume"

## v1.3.2
|||
|---|---|
|Date|2022-02-10
|Kind| Bugfix release
|Author|mschiess@akamai.com
- **Features**
  - Kubernetes deployment example / Helm charts added ([start here](KUBERNETES_USAGE.md))  
  

- **Minor improvements**
  - Bumped ETP-CLI to version 0.3.7 in Dockerfile
  - Bumped EAA-CLI version to 0.4.6 in Dockerfile  
  

- **Bugfixes**
  - fixed issue when using file handler and rotation at "midnight" - running back in time for 30 days
  - added a sanity (dictionary) check for "--httpauthheader"
  - fixed a bug in http reconnecting forever in certain circumstances
  - added a sanity check for "HTTP_OUT_FORMAT" to avoid issues with the ´%s´ seclector
  - removed forced http authentication token "--httpauthheader" (allow None)
  - discovered a bug in configparser -> [see FAQ entry](FAQ.md#uls-does-not-start-due-to-missing-field-in-config)


## v1.3.1
|||
|---|---|
|Date|2021-12-20
|Kind| Bugfix release
|Author|mschiess@akamai.com
- **Bugfixes**
  - fixed a checkpoint issue when using ETP / THREAD 
  - some doc fixes

## v1.3.0
|||
|---|---|
|Date|2021-12-17
|Kind| Feature & Bugfix release
|Author|mschiess@akamai.com
- **Features**
  - [internal] Added automated test scripts to improve continuous release quality
  - [AUTO-RESUME feature](ADDITIONAL_FEATURES.md#autoresume--resume) enables ULS to automatically continue operation starting from the last saved checkpoint.
  - [FileAction support](ADDITIONAL_FEATURES.md#post-processing-of-files-fileoutput-only) to trigger custom scripts upon file rotation event.


- **Minor improvements**
  - Bumped ETP-CLI to version 0.3.6 in Dockerfile
  - Bumped EAA-CLI version to 0.4.5 in Dockerfile
  - Added additional fields to the monitoring output ([uls_version, event_count_interval](MONITORING.md))


- **Bugfixes**
  - removed hard requirement to run ULS via bin/uls.py - can now be run from everywhere 
  - introduced HTTP Timeout (for HTTP OUTPUT) to the configuration file (http stream did not issue proper error messages in some cases)
  - Fixed an output issue on "CLI failure", added configureable output handling to the config
  - replaced pip with pip3 in CLI usage docs
  - Fixed a windows bug (bypass blocking on windows) + added a [FAQ entry on how fix a installation specific bug](FAQ.md#uls-on-windows-error-winerror-2-the-system-cannot-find-the-file-specified)


## v1.2.0
|||
|---|---|
|Date|2021-11-02
|Kind| Feature & Bugfix release
|Author|mschiess@akamai.com, adrocho@akamai.com
- **Features**
  - [Transformation Support for output format transformation ](TRANSFORMATIONS.md)(additional log formats and integrations) introduced
  - [MCAS transformation](TRANSFORMATIONS.md#microsoft-cloud-application-security-mcas): Microsoft Cloud Application Security
  - [JMESPATH transformation](TRANSFORMATIONS.md#jmespath): Create your own pattern / filter / searches
  - added [--starttime ](ARGUMENTS_ENV_VARS.md#input)to tell ULS where to start scratching the logs (EPOCH time required)
  - added [--endtime](ARGUMENTS_ENV_VARS.md#input) to allow cherry-picking of a specific time-slice (EPOCH time required)
  - added [FILE OUTPUT ](OUTPUTS.md#file)support (writes log streams to a file to the local filesystem)
- **Bugfix**
  - Fixed a bug in proxy handling (using cli param), re-enabled CLI cmd and amended docs
  - Fixed a bug that prevented "--version" to work properly
  - Fixed a bug that mitigates version display bug on the CLI (solves the symptom only)
  - Fixed a bug that potentially allowed buffered output from the CLI's (CLI calls and DOCKERFILE)
- **Minor improvements**
  - updated base container to "python:3.10-slim-bullseye"  ****
  - Introduced "systemd" example to [Command Line Usage docs](COMMAND_LINE_USAGE.md#uls-as-a-service-systemd)
  - Introduced docker check to version check and amendment to UA Header
  - Introduced - Message re-transmission on network error
  - ReFactored INPUT / OUTPUT handler to reduce compute & memory footprint
  - bumped EAA CLI Version to 0.4.4 (docker only)
  - Introduced dedicated ["OUTPUT" documentation](OUTPUTS.md)
  - introduced uls own requirements.txt in the [bin directory](../bin/requirements.txt) - still trying to keep req's as low as possible. 
  
## v1.1.0
|||
|---|---|
|Date|2021-08-18
|Kind|Bugfix / Feature
|Author|mschiess@akamai.com
- **Features**
  - Added **DNS** and **PROXY** feeds to ETP Input (<3 Sara)
- **Minor improvements**
  - Version number fix (Stated 0.9.0 instead of 1.x.x)
  - debug "message" fix ( changed HTTP to HTTP(S) to avoid misunderstanding)
  - documented workaround for discovered proxy issue
  - enabled json highlighting in [Log_overview](./LOG_OVERVIEW.md)
  - added better error guidance when basic stuff is unset (input / output)
  - moved docker-compose from root dir to /docs
  - added `read_only: true` to the docker-compose.yml files (security enhancement)

## v1.0.0
|||
|---|---|
|Date|2021-08-10
|Kind|Bugfix / Feature
|Author|mschiess@akamai.com, adrocho@akamai.com
- **Minor improvements**
  - EdgeRC file check (preflight) and "~" expansion to solve some common issues
  - fixed some typos in the "docker-compose" file
  - bumped EAA-CLI to version 0.4.2
  - simplified cli - command re-usage (visual parsing of subprocess cmd)
  - cleaned up the Dockerfile
  - added [Log_Overview](LOG_OVERVIEW.md) page to extend background on logged data


## v0.9.0
|||
|---|---|
|Date|2021-07-26-2021
|Kind|Bugfix / Feature
|Author|mschiess@akamai.com, adrocho@akamai.com
- Minor improvements 
  - fixed some typos / instructions
  - bumped EAA version to 0.4.1
  - bumped MFA version to 0.6.0
  - updated docker base image to python/3.9.6-slim-buster
  - Added API Credentials documentation
  - fixed a bug in rawcmd handling
  - Improved cli input error handling to leverage "restarting" towards docker
  - added FAQ documents
- Feature:
  - [FILTER (--filter) feature](ADDITIONAL_FEATURES.md#filter---filter-feature) introduced to reduce number of sent log lines towards SIEM
  

## v0.0.4
|||
|---|---|
|Date|2021-06-17
|Kind|Bugfix / Feature
|Author|mschiess@akamai.com
- Minor improvements 
  - Wait_time and wait_max shifted to config
  - added -f flag as alternative to --flag
  - fixed an exception that was introduced in v0.0.3
  - bumped MFA -CLI to 0.0.5 in dockerfile
  - added an additional debugging example
- Feature:
  - EAA CONNECTOR HEALTH (CONHEALTH) now available
  - Preflight (forced) check for available cli's

## v0.0.3
|||
|---|---|
|Date|2021-06-15
|Kind|Bugfix / Feature
|Author|mschiess@akamai.com <br> adrocho@akamai.com
- introduced line breaker variable for output
- fixed a bug in the "poll" handling
- fixed a bug that caused Popen PIPE to hang in certain circumstances
- bumped Dockerfile to newer CLI versions
- [introduced RAW output](ADDITIONAL_FEATURES.md#rawcmd---rawcmd-feature) (send data to stdout)

## v0.0.2
|||
|---|---|
|Date|2021-06-10
|Kind|Bugfix
|Author|mschiess@akamai.com <br> adrocho@akamai.com
- fixed monitoring output bug in docker-compose
- fixed bug in Dockerfile that prevented development builds
- fixed a bug in EAA CLI handler

## v0.0.1 (Initial Commit)
|version|v0.0.1|
|---|---|
|Date|2021-06-09
|Kind|Initial Commit
|Author|mschiess@akamai.com <br> adrocho@akamai.com
- INPUT: EAA, ETP, MFA (based on CLI's)
- OUTPUT: HTTP, TCP, UDP
- Docker & docker-compose examples
- Error & Reconnection handling
- Monitoring hook introduced Example:
- Kill Signal handling
- Configuration file `bin/config/global_config.py`
- Documentation & usage examples