import subprocess
from argparse import Namespace
from pathlib import Path
from shlex import quote
from time import sleep

from decouple import Config, RepositoryEnv
from tqdm import trange

from wsl2p_remote.utils import replace_line_with, search_string_in_file


def run(args: Namespace):
    # variables import from .env file
    # should be in script arg?
    DOTENV_FILE = Path(__file__).parent / ".." / ".env"
    config = Config(RepositoryEnv(DOTENV_FILE))

    # win_host = config("SERVER_WIN_HOST")
    wsl_host = config("SERVER_WSL_HOST")

    server_win_user = config("SERVER_WIN_USER")
    server_win_ip = config("SERVER_WIN_IP")
    server_win_mac = config("SERVER_WIN_MAC")

    rpi_ip = config("RPI_IP")
    rpi_user = config("RPI_USER")

    # server_wsl_user = config("SERVER_WSL_USER")
    client_win_user = config("CLIENT_WIN_USER")

    ssh_config_client = f"/mnt/c/Users/{client_win_user}/.ssh/config"
    ssh_config_server = r"C:\Users\{}\.ssh\config".format(
        server_win_user,
    )  # can't use f-string with backslash

    sleep_time = args["SLEEP_TIME"]
    sleep_increment = 0.1

    hostname_server_win = f"{server_win_user}@{server_win_ip}"
    hostname_rpi = f"{rpi_user}@{rpi_ip}"

    # send WakeOnLan through client-side windows host
    # requires port forwarding...
    # subprocess.run(["powershell.exe", "Invoke-WakeOnLan", server_win_mac])

    # use rpi on LAN to send WOL
    subprocess.run(["ssh", hostname_rpi, "wakeonlan", server_win_mac])

    # sleep to wait for boot and wsl startup
    # cannot find an elegant way to check if wsl has started
    print("Wait for server boot ...")
    for i in trange(int(sleep_time // sleep_increment)):
        sleep(sleep_increment)

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
    matches = search_string_in_file(
        file_name=ssh_config_client,
        string_to_search=wsl_host,
    )
    linenum_client = matches[0][0] + 1

    replace_line_with(
        file_name=ssh_config_client,
        line_number=linenum_client,
        new_line=line_server,
    )
