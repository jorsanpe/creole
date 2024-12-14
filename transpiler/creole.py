#!/usr/bin/env python
import argparse
import sys
from creole.commands.run import run
from creole.commands.transpile import transpile


def top_level_parser():
    parser = argparse.ArgumentParser(description='creole: an opinionated programming language')
    parser.add_argument('-v', '--version',
                        action='version',
                        help='show version and exit')
    parser.add_argument('command',
                        choices=['run', 'transpile'],
                        nargs=argparse.REMAINDER)
    return parser


commands = {
    'run': run,
    'transpile': transpile
}


def main():
    args = top_level_parser().parse_args(sys.argv[1:])

    if not args.command:
        print('invalid command')
        sys.exit(0)

    command_to_execute = args.command[0]
    command_arguments = args.command[1:]

    commands[command_to_execute](command_arguments)


if __name__ == '__main__':
    main()
