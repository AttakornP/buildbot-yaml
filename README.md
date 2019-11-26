![](https://github.com/AttakornP/buildbot-yaml/workflows/Python%20application/badge.svg)

# How to Setup Buildbot by YAML Config

  * Easy to setup basic Buildbot config.

### Requirement packages 
  * buildbot
  * buildbot-slave
  * python-git
  * python-yaml

### Limitation
  * Can not clone project to other name.
  * This version support only shell command.
  * This version not support Git with out upstream.

### How to use 
1. Create `config.yml` in project's root folder.
1. Clone code from this repository to server.
1. run script  
``` create-buildbot <project_repository> <branch> ```
1. Verify by go to waterfall page and try to force build.

### YAML config format
```
git:
-
  repository : git@<host>:<namespace>/<projectname>.git
  branch : <develop>

project_name:
- <projectname>

master_host:
- <master ip>

builder:
- 
  name : slave-name
  password : slave-password

mail_list:
- <team@mail.com>

relation:
  <projectname> :
  - <builder[name]>

factory:
  <builder[name]>:
  -
    command : <shell cmd>
    workdir : <dir for use cmd>
  -
    command : <shell cmd>
    workdir : <dir for use cmd>
```
