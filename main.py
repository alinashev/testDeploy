import argparse
import sys

from Action.Router import Router


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v')
    return parser


def main():
    print("Hello jenkins!!!!")
    parser = createParser()
    version = parser.parse_args(sys.argv[1:])
    param = version.v

    router = Router(int(param))
    router.generate_menu()
    router.selection_version()


if __name__ == '__main__':
    main()
