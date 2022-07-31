from argparse import ArgumentParser, Namespace

from wsl2p_remote.client_side import run
from wsl2p_remote.install import config, install, uninstall
from wsl2p_remote.server_side import update


class MyParser(ArgumentParser):
    def printhelp(self, args: Namespace):
        self.print_help()


def main():
    parser = MyParser()
    parser.set_defaults(func=parser.printhelp)
    subparsers = parser.add_subparsers(help="sub-command help")

    # run
    parser_run = subparsers.add_parser(
        "run",
        help="WOL server and update client-side .ssh/config",
    )
    parser_run.add_argument(
        "-t",
        "--sleep_time",
        help="time (s) to wait for server to boot and start WSL",
        default=60,
    )
    parser_run.set_defaults(func=run)

    # update
    parser_update = subparsers.add_parser(
        "update",
        help="update server-side .ssh/config",
    )
    parser_update.set_defaults(func=update)

    # install
    parser_install = subparsers.add_parser(
        "install",
        help="install the settings file and required stuff",
    )

    parser_install.set_defaults(func=install)
    parser_install_options = parser_install.add_mutually_exclusive_group()
    parser_install_options.add_argument("--client", action="store_true")
    parser_install_options.add_argument("--server", action="store_true")

    # config
    parser_config = subparsers.add_parser(
        "config",
        help="edit settings file",
    )

    parser_config.set_defaults(func=config)

    # uninstall
    parser_uninstall = subparsers.add_parser(
        "uninstall",
        help="get the system back to original place",
    )
    parser_uninstall_options = parser_uninstall.add_mutually_exclusive_group()
    parser_uninstall_options.add_argument("--client", action="store_true")
    parser_uninstall_options.add_argument("--server", action="store_true")
    parser_uninstall_options.set_defaults(func=uninstall)

    args = parser.parse_args()
    args.func(args)
