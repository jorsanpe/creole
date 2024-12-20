import unittest
import textwrap
from creole.entry import transpile
import difflib
import os


def dedent(string):
    return textwrap.dedent(string).strip()


class TestFunction(unittest.TestCase):
    def test_transpilations(self):
        for filename in os.listdir("test/c_transpiler"):
            with self.subTest(filename, filename=filename):
                with open(f'test/c_transpiler/{filename}', "r") as stream:
                    full = stream.read()
                split = full.split("------")
                if len(split) == 2:
                    creole, c_code = split
                elif len(split) == 3:
                    creole, c_code, header_code = split

                transpiler_header, transpiled_source = transpile(creole, "C")

                if transpiled_source != c_code.lstrip():
                    print(f'error: {filename}. Transpiled code does not match expectation')
                    print(get_edits_string(c_code.lstrip(), transpiled_source))

                if len(split) == 3:
                    if transpiler_header != header_code.lstrip():
                        print(f'error: {filename}. Transpiled header does not match expectation')
                        print(get_edits_string(header_code.lstrip(), transpiler_header))


def get_edits_string(old, new):
    def red(text):
        return f"\033[38;2;255;0;0m{text}\033[38;2;255;255;255m"

    def blue(text):
        return f"\033[38;2;0;100;255m{text}\033[38;2;255;255;255m"

    def white(text):
        return f"\033[38;2;255;255;255m{text}\033[38;2;255;255;255m"

    result = ""
    codes = difflib.SequenceMatcher(a=old, b=new).get_opcodes()
    for code in codes:
        if code[0] == "equal":
            result += white(old[code[1]:code[2]])
        elif code[0] == "delete":
            result += red(old[code[1]:code[2]])
        elif code[0] == "insert":
            result += blue(new[code[3]:code[4]])
        elif code[0] == "replace":
            result += (red(old[code[1]:code[2]]) + blue(new[code[3]:code[4]]))
    return result
