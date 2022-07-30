from argparse import ArgumentParser, Namespace

from wsl2p_remote.client_side import run
from wsl2p_remote.install import install, uninstall


class MyParser(ArgumentParser):
    def printhelp(self, args: Namespace):
        self.print_help()


def main():
    parser = MyParser()
    parser.set_defaults(func=parser.printhelp)
    subparsers = parser.add_subparsers(help="sub-command help")

    # install
    parser_install = subparsers.add_parser(
        "install",
        help="install the settings file and required stuff",
    )

    parser_install.set_defaults(func=install)
    parser_install_options = parser_install.add_mutually_exclusive_group()
    parser_install_options.add_argument("--client", action="store_true")
    parser_install_options.add_argument("--server", action="store_true")

    # uninstall
    parser_uninstall = subparsers.add_parser(
        "uninstall",
        help="get the system bach to original place",
    )
    parser_uninstall_options = parser_uninstall.add_mutually_exclusive_group()
    parser_uninstall_options.add_argument("--client", action="store_true")
    parser_uninstall_options.add_argument("--server", action="store_true")
    parser_uninstall_options.set_defaults(func=uninstall)

    # run
    parser_run = subparsers.add_parser(
        "run",
        help="send WOL packet and update server ip",
    )
    parser_run.set_defaults(func=run)

    args = parser.parse_args()
    args.func(args)
