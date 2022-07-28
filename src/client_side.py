#! /home/antoine/miniconda3/envs/wsl2remote/bin/python3
import subprocess
from pathlib import Path
from shlex import quote

from decouple import Config, RepositoryEnv

from utils import replace_line_with, search_string_in_file

# variables import from .env file
# should be in script arg?
DOTENV_FILE = Path(__file__).parent / ".." / ".env"
config = Config(RepositoryEnv(DOTENV_FILE))

win_host = config("SERVER_WIN_HOST")
wsl_host = config("SERVER_WSL_HOST")

server_win_user = config("SERVER_WIN_USER")
server_win_ip = config("SERVER_WIN_IP")
server_win_mac = config("SERVER_WIN_MAC")

server_wsl_user = config("SERVER_WSL_USER")
client_win_user = config("CLIENT_WIN_USER")

ssh_config_client = f"/mnt/c/Users/{client_win_user}/.ssh/config"
ssh_config_server = r"C:\Users\{}\.ssh\config".format(
    server_win_user,
)  # can't use f-string with backslash

hostname_server_win = f"{server_win_user}@{server_win_ip}"

# send WakeOnLan through client-side windows host
subprocess.run(["powershell.exe", "Invoke-WakeOnLan", server_win_mac])

# ssh to server and read .ssh/config
command2 = ["Get-Content", ssh_config_server]
command2_str = " ".join(quote(n) for n in command2)
command1 = [
    "ssh",
    "-T",
    hostname_server_win,
    command2_str,
]  # capital T is super important

sshconf_read = (
    subprocess.run(command1, shell=False, capture_output=True)
    .stdout.decode("utf-8")
    .splitlines()
)


# find hostname in server-side /.ssh/config
matches = [x for x in enumerate(sshconf_read) if wsl_host in x[1]]
line_server = sshconf_read[matches[0][0] + 1] + "\n"

# write to client-side /.ssh/config
matches = search_string_in_file(file_name=ssh_config_client, string_to_search=wsl_host)
linenum_client = matches[0][0] + 1

replace_line_with(
    file_name=ssh_config_client,
    line_number=linenum_client,
    new_line=line_server,
)
