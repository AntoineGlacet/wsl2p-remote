import subprocess
from pathlib import Path

from decouple import Config, RepositoryEnv

from wsl2p_remote.utils import replace_line_with, search_string_in_file

# variables import from .env file
# should be in script arg?
DOTENV_FILE = Path(__file__).parent / ".." / ".env"
config = Config(RepositoryEnv(DOTENV_FILE))

wsl_host = config("SERVER_WSL_HOST")
server_win_user = config("SERVER_WIN_USER")


ssh_config_server = f"/mnt/c/Users/{server_win_user}/.ssh/config"


# find server-side wsl hostname ip
new_hostip = subprocess.run(["hostname", "-I"], capture_output=True).stdout.decode(
    "utf-8",
)
new_line = f"    Hostname {new_hostip}"

# write to server-side /.ssh/config
matches = search_string_in_file(file_name=ssh_config_server, string_to_search=wsl_host)
linenum = matches[0][0] + 1

replace_line_with(
    file_name=ssh_config_server,
    line_number=linenum,
    new_line=new_line,
)
