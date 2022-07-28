# ssh-to-wsl2preview

## description

scripts to connect WSl => WSL preview with ssh

From client-side:
1. Wake-on-lan server
2. Wait server hostname ip update
3. Update client %USERPROFILE%/.ssh/config file

From server-side:
1. at WSL start
2. update server %USERPROFILE%/.ssh/config file



## Prerequesite
1. install wakeonlan
`sudo apt install wakeolan`

1. set windows local machine execution to RemoteSigned
(req. admin rights to change permession)
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine`

2. active open-ssh on windows enable and register pulic keys

bug: delete weird line from ssh_config file (at the end)

task sheduler for starting wsl


add wake on lan to functions on client-side host windows


## Why it sucks

1. need admin privilege on both client and server to setup (not to connect)
2. go through a lot of steps and things to do something simple

