import io
from creole.creole_parserListener import creole_parserListener
from creole.creole_parser import creole_parser


INDENT = 4


class Transpiler(creole_parserListener):

    def __init__(self):
        self.output_stream = io.StringIO()
        self.indent = 0

    def enterFunction(self, ctx: creole_parser.FunctionContext):
        function_identifier = ctx.children[1]
        self.emit(f'void {function_identifier}(void) {{')
        self.indent += INDENT

    def exitFunction(self, ctx: creole_parser.FunctionContext):
        self.indent -= INDENT
        self.emit('}')

    def enterFunctionCall(self, ctx: creole_parser.FunctionCallContext):
        identifier = ctx.children[0]
        function_arguments = ctx.children[2]
        first_function_argument = function_arguments.children[0]
        first_function_argument_string = first_function_argument.children[0]

        # if identifier == "print":
        self.emit(f'printf({first_function_argument_string});')
        self.emit(f'printf("\\n");')

    def transpiled(self):
        return self.output_stream.getvalue()

    def emit(self, code):
        self.output_stream.write(f'{" "*self.indent}{code}')
        self.output_stream.write("\n")
