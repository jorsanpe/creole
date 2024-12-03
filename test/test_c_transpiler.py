import unittest
import textwrap
from creole.entry import transpile


def dedent(string):
    return textwrap.dedent(string).strip()


class TestFunction(unittest.TestCase):
    def test_function_implementation(self):
        source_code = dedent("""
        fn main() {
        }
        """)

        transpiled = dedent(
            transpile(source_code, "C")
        )
        expected = dedent("""
        void main() {
        }
        """)
        self.assertEqual(transpiled, expected)
