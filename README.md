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
install wakeonlan
`sudo apt install wakeolan`

set windows local machine execution to RemoteSigned
(req. admin rights to change permession)
`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine`

intall open-ssh on windows&linux enable and register pulic keys, make sure service start (wsl.conf boot and Powershell command)
bug: delete weird line from ssh_config file (at the end) on windows for public key login to not fail
task sheduler for starting wsl ==> does not work yet
add wake on lan to functions on client-side host windows

3. add server-side.py to wsl.conf `[boot]` category

## Why it sucks

1. need admin privilege on both client and server to setup (not to connect)
2. go through a lot of steps and things to do something simple

## Why it sucks even more

1. need to set passwordless login for windows server user (cannot start wsl at boot without user login...)
2. need to go through raspberry pi to wake-on-lan (or do some port forwarding because openVPM / wakeonlan)

## to do
clean, document, make it usable by someone in same use case rather simply.
deal with the env, dependency and packaging...


## format of .ssh/config

The file must follow this format on both client and server side

```
# Read more about SSH config files: https://linux.die.net/man/5/ssh_config

Host My_windows_PC            # anything is fine
    HostName 192.168.0.42     # lan IP of server (from ipconfig)
    User john                 # windows username

Host My_wsl_distribution     # anything is fine
    Hostname 172.31.8.179    # will be rewriten by script
	User doe                 # wsl username
    ProxyCommand ssh -W %h:%p My_windows_PC    # should be windows host
```
