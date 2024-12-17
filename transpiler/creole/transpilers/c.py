import io
import antlr4

from creole.antlr.creole_parserListener import creole_parserListener
from creole.antlr.creole_parser import creole_parser


INDENT = 4


class Transpiler(creole_parserListener):

    def __init__(self):
        self.header_stream = io.StringIO()
        self.header_block_stream = io.StringIO()
        self.source_block_stream = io.StringIO()
        self.indent = 0
        self.print_function = False
        self.dependency_list = []
        self.namespace_path = []
        self.function_arguments = []

    def exitHeaderBlock(self, ctx: creole_parser.HeaderBlockContext):
        for dependency in self.dependency_list:
            header = dependency.symbol.text.replace('"', '') + ".h"
            self.emit_include(header)

    def enterDependency(self, ctx: creole_parser.DependencyContext):
        self.dependency_list.append(ctx.children[0])

    def enterNamespace(self, ctx: creole_parser.NamespaceContext):
        namespace_identifier = ctx.children[1]
        self.namespace_path.append(namespace_identifier)

    def exitNamespace(self, ctx: creole_parser.NamespaceContext):
        self.namespace_path.pop()

    def enterFunction(self, ctx: creole_parser.FunctionContext):
        function_identifier = self.first_identifier(ctx)
        function_name = self.function_name(function_identifier)
        self.emit(f'void {function_name}(void) {{')
        self.indent += INDENT
        self.print_function = False

    def exitFunction(self, ctx: creole_parser.FunctionContext):
        self.indent -= INDENT
        self.emit('}')

    def enterFunctionCall(self, ctx: creole_parser.FunctionCallContext):
        namespace_path = self.namespace_reference(ctx.children[0])
        identifier = self.first_identifier(ctx)
        if identifier.symbol.text == "print":
            self.emit_include("stdio.h")
            self.emit_start(f'printf(')
            self.print_function = True
        else:
            self.emit_start(f'{self.function_call_name(namespace_path, identifier)}(')

    def namespace_reference(self, ctx):
        if isinstance(ctx, antlr4.TerminalNode):
            return []

        return self.build_namespace_path(ctx)

    def build_namespace_path(self, ctx):
        if isinstance(ctx, antlr4.TerminalNode):
            return [ctx]

        if ctx.children[0].getRuleIndex() == creole_parser.RULE_namespaceReference:
            return self.build_namespace_path(ctx.children[0]) + [ctx.children[1].children[0]]

        return [ctx.children[0].children[0]]

    def enterFunctionArguments(self, ctx: creole_parser.FunctionArgumentsContext):
        self.function_arguments = []
        # function_arguments = ctx
        # if function_arguments.children:
        #     first_function_argument = function_arguments.children[0]
        #     first_function_argument_string = first_function_argument.children[0]
        #     self.emit_partial(f'{first_function_argument_string}')

    def enterFunctionArgument(self, ctx: creole_parser.FunctionArgumentContext):
        self.function_arguments.append(ctx.children[0])

    def exitFunctionCall(self, ctx: creole_parser.FunctionCallContext):
        self.emit_end(');')
        if self.print_function:
            self.emit(f'printf("\\n");')

    def first_identifier(self, context):
        for node in context.children:
            if hasattr(node, 'symbol') and node.symbol.type == creole_parser.Identifier:
                return node
        return None

    def function_name(self, identifier):
        return "_".join(
            map(
                lambda ident: ident.symbol.text,
                self.namespace_path + [identifier]
            )
        )

    def function_call_name(self, namespace, identifier):
        return "_".join(
            map(
                lambda ident: ident.symbol.text,
                namespace + [identifier]
            )
        )

    def transpiled(self):
        return self.header_code(), self.source_code()

    def header_code(self):
        return self.header_stream.getvalue()

    def source_code(self):
        return f'{self.header_block_stream.getvalue()}{self.source_block_stream.getvalue()}'

    def emit_include(self, header):
        self.header_block_stream.write(f'#include <{header}>\n')

    def emit_start(self, code):
        self.source_block_stream.write(f'{" " * self.indent}{code}')

    def emit_end(self, code):
        self.source_block_stream.write(code)
        self.source_block_stream.write("\n")

    def emit_partial(self, code):
        self.source_block_stream.write(code)

    def emit(self, code):
        self.source_block_stream.write(f'{" " * self.indent}{code}')
        self.source_block_stream.write("\n")
