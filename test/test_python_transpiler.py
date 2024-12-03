import unittest
import textwrap
from creole.entry import transpile
import os


def dedent(string):
    return textwrap.dedent(string).strip()


class TestFunction(unittest.TestCase):
    def test_transpilations(self):
        for filename in os.listdir("test/c_transpiler"):
            with open(f'test/c_transpiler/{filename}', "r") as stream:
                full = stream.read()
            creole, python = full.split("------")

            transpiled = transpile(creole, "python")

            self.assertEqual(transpiled, python.lstrip())
