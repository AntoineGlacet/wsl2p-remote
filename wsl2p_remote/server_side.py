import subprocess
from argparse import Namespace
from configparser import ConfigParser
from pathlib import Path

from wsl2p_remote.utils import replace_line_with, search_string_in_file


def update(args: Namespace):
    # config from file
    dotconf = Path.home() / ".config/wsl2p-remote/conf.ini"
    config = ConfigParser()
    config.read(dotconf)

    wsl_host = config["host"]["SERVER_WSL_HOST"]
    server_win_user = config["host"]["SERVER_WIN_USER"]
    ssh_config_server = f"/mnt/c/Users/{server_win_user}/.ssh/config"

    # find server-side wsl hostname ip
    new_hostip = (
        subprocess.run(["hostname", "-I"], capture_output=True)
        .stdout.decode(
            "utf-8",
        )
        .split(" ")[0]
    )
    nl = "\n"
    new_line = f"    Hostname {new_hostip}{nl}"

    # write to server-side /.ssh/config
    matches = search_string_in_file(
        file_name=ssh_config_server,
        string_to_search=wsl_host,
    )
    linenum = matches[0][0] + 1

    replace_line_with(
        file_name=ssh_config_server,
        line_number=linenum,
        new_line=new_line,
    )
    return
