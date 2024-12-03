import sys
from creole import entry


def main(argv):
    with open(argv[1], "r") as stream:
        source_code = stream.read()
    entry.transpile(source_code, "python")


if __name__ == '__main__':
    main(sys.argv)
