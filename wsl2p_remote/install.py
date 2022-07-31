from argparse import Namespace


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
    return
