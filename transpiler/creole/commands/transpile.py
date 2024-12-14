import argparse
from creole import entry


def transpile(argv):
    args = argument_parser().parse_args(argv)

    with open(args.input_file, "r") as stream:
        source_code = stream.read()
    transpiled = entry.transpile(source_code, args.language)
    print(transpiled)


def argument_parser():
    parser = argparse.ArgumentParser(prog='creole', description='invoke the creole parser')
    parser.add_argument('-o', '--output-file', help='output file')
    parser.add_argument('-l', '--language', help='output language', default="C", choices=["C", "python"])
    parser.add_argument('input_file', help='input files')
    return parser
