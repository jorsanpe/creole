import unittest
import textwrap
from creole.entry import transpile
import os


def dedent(string):
    return textwrap.dedent(string).strip()


class TestFunction(unittest.TestCase):
    def test_transpilations(self):
        for filename in os.listdir("test/python_transpiler"):
            with self.subTest(filename, filename=filename):
                with open(f'test/python_transpiler/{filename}', "r") as stream:
                    full = stream.read()
                creole, python = full.split("------")

                transpiled = transpile(creole, "python")

                self.assertEqual(
                    transpiled,
                    python.lstrip(),
                    f'{filename}'
                )
