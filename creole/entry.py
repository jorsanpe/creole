from antlr4 import *
from creole.creole_lexer import creole_lexer
from creole.creole_parser import creole_parser
from creole.transpilers import c, python


def transpile(source_code, target_language):
    input_stream = InputStream(source_code)
    lexer = creole_lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = creole_parser(token_stream)
    tree = parser.function()
    transpiler = None
    if target_language == "C":
        transpiler = c.Transpiler()
    elif target_language == "python":
        transpiler = python.Transpiler()

    walker = ParseTreeWalker()
    walker.walk(transpiler, tree)

    return transpiler.transpiled()
