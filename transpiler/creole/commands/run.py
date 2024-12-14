import argparse
import os
import subprocess

from creole import entry
from creole import cmakelists


def create_build_directory(project_name):
    os.makedirs(f'build', exist_ok=True)
    with open('build/CMakeLists.txt', 'w') as stream:
        stream.write(cmakelists.cmakelists(project_name))


def transpile_file(filename, language):
    with open(filename, "r") as stream:
        source_code = stream.read()
    transpiled = entry.transpile(source_code, language)
    output_filename = f"build/{filename.replace('.cre', '.c')}"
    with open(output_filename, 'w') as stream:
        stream.write(transpiled)


def build_project(project_name):
    subprocess.run(['cmake', '-G', 'Ninja', '-B', 'build', 'build'], stdout=subprocess.DEVNULL)
    subprocess.run(['ninja', project_name], cwd='build', stdout=subprocess.DEVNULL)
    subprocess.run(['./creole'], cwd='build/bin')


def run(argv):
    args = argument_parser().parse_args(argv)

    project_name = 'creole'

    create_build_directory(project_name)
    transpile_file('main.cre', args.language)
    build_project(project_name)


def argument_parser():
    parser = argparse.ArgumentParser(prog='creole', description='run a creole program')
    parser.add_argument('-l', '--language', help='output language', default="C", choices=["C", "python"])
    return parser
