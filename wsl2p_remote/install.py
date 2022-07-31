from argparse import Namespace
from configparser import ConfigParser
from pathlib import Path

from wsl2p_remote.utils import colors


def install(args: Namespace):
    if args.client:
        print(
            """
        create the config file from .env
        fills some default values
        interactively fills missing values
        """,
        )
    if args.server:
        print(
            """
        check requirements
        set default values
        """,
        )
    else:
        print("need to choose server or client")
    return


def uninstall(args: Namespace):
    print(args)
    if not (args.client and args.server):
        print("need to choose server or client")
    else:
        print(
            """
        not done yet
        """,
        )
    return


def config(args: Namespace):
    # interactive config and info
    print(
        """This command will edit the config file located at ~/.config/wslp-remote/config.conf
    leave blank to keep value""",
    )

    dotconf = Path.home() / ".config/wsl2p-remote/conf.ini"
    dotconf_example = Path(__file__).parents[0] / "resource/conf.ini.example"
    dotconf.parent.mkdir(parents=True, exist_ok=True)

    # if does not exist, create as example
    if not dotconf.exists():
        dotconf.touch(mode=0o666)
        with dotconf_example.open() as file:
            data_orig = file.readlines()
        with dotconf.open(mode="w") as file:
            file.writelines(data_orig)
    else:
        with dotconf.open() as file:
            data_orig = file.readlines()

    config = ConfigParser()
    config.read(dotconf)

    # user input
    for section in config.sections():
        for key, value in config[section].items():
            x = input(
                f"Enter {colors.fg.lightblue}{key}{colors.reset} (currently ="
                f" {colors.fg.lightcyan}{value}{colors.reset}): ",
            )
            if not x.strip():
                print(f"keep current value = {colors.fg.green}{value}{colors.reset}")
            else:
                config[section][key] = x.strip()
                print(f"new value = {colors.fg.green}{x.strip()}")
    # selectively  replace
    data = [x for x in data_orig]
    for section in config.sections():
        for key, value in config[section].items():
            matches = [x for x in enumerate(data_orig) if key.lower() in x[1].lower()]
            for match in matches:
                data[match[0]] = f"{key} = {value}\n"
    with dotconf.open(mode="w") as file:
        file.writelines(data)
