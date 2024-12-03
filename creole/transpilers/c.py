import io
from creole.creole_parserListener import creole_parserListener
from creole.creole_parser import creole_parser


INDENT = 2


class Transpiler(creole_parserListener):

    def __init__(self):
        self.output_stream = io.StringIO()
        self.indent = 0

    def enterFunction(self, ctx: creole_parser.FunctionContext):
        function_identifier = ctx.children[1]
        self.emit(f'void {function_identifier}() {{')
        self.indent += INDENT

    def exitFunction(self, ctx: creole_parser.FunctionContext):
        self.emit('}')

    def transpiled(self):
        return self.output_stream.getvalue()

    def emit(self, code):
        self.output_stream.write(code)
        self.output_stream.write("\n")
