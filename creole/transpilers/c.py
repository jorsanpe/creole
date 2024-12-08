import io
from creole.antlr.creole_parserListener import creole_parserListener
from creole.antlr.creole_parser import creole_parser


INDENT = 4


class Transpiler(creole_parserListener):

    def __init__(self):
        self.output_stream = io.StringIO()
        self.indent = 0
        self.print_function = False

    def enterFunction(self, ctx: creole_parser.FunctionContext):
        function_identifier = ctx.children[1]
        self.emit(f'void {function_identifier}(void) {{')
        self.indent += INDENT
        self.print_function = False

    def exitFunction(self, ctx: creole_parser.FunctionContext):
        self.indent -= INDENT
        self.emit('}')

    def enterFunctionCall(self, ctx: creole_parser.FunctionCallContext):
        identifier = ctx.children[0]
        if identifier.symbol.text == "print":
            self.emit_start(f'printf(')
            self.print_function = True
        else:
            self.emit_start(f'{identifier}(')

    def enterFunctionArguments(self, ctx: creole_parser.FunctionArgumentsContext):
        function_arguments = ctx
        if function_arguments.children:
            first_function_argument = function_arguments.children[0]
            first_function_argument_string = first_function_argument.children[0]
            self.emit_partial(f'{first_function_argument_string}')

    def exitFunctionArguments(self, ctx: creole_parser.FunctionArgumentsContext):
        self.emit_end(');')
        if self.print_function:
            self.emit(f'printf("\\n");')

    def transpiled(self):
        return self.output_stream.getvalue()

    def emit_start(self, code):
        self.output_stream.write(f'{" "*self.indent}{code}')

    def emit_end(self, code):
        self.output_stream.write(code)
        self.output_stream.write("\n")

    def emit_partial(self, code):
        self.output_stream.write(code)

    def emit(self, code):
        self.output_stream.write(f'{" "*self.indent}{code}')
        self.output_stream.write("\n")
