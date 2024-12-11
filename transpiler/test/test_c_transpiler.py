import unittest
import textwrap
from creole.entry import transpile
import os


def dedent(string):
    return textwrap.dedent(string).strip()


class TestFunction(unittest.TestCase):
    def test_transpilations(self):
        for filename in os.listdir("test/c_transpiler"):
            with self.subTest(filename, filename=filename):
                with open(f'test/c_transpiler/{filename}', "r") as stream:
                    full = stream.read()
                creole, c_code = full.split("------")

                transpiled = transpile(creole, "C")

                self.assertEqual(
                    transpiled,
                    c_code.lstrip(),
                    f'{filename}'
                )

