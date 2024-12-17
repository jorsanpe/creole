from antlr4 import *
from creole.antlr.creole_lexer import creole_lexer
from creole.antlr.creole_parser import creole_parser
from creole.transpilers import c


def transpile(source_code, target_language):
    input_stream = InputStream(source_code)
    lexer = creole_lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = creole_parser(token_stream)
    tree = parser.program()
    transpiler = c.Transpiler()

    walker = ParseTreeWalker()
    walker.walk(transpiler, tree)

    return transpiler.transpiled()
