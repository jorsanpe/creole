import io
from creole.antlr.creole_parserListener import creole_parserListener
from creole.antlr.creole_parser import creole_parser
from creole.transpilers import emitter

INDENT = 4


class Transpiler(creole_parserListener):

    def __init__(self):
        self.source_emitter = emitter.Emitter()
        self.header_emitter = emitter.Emitter()

        # self.header_stream = io.StringIO()
        # self.header_block_stream = io.StringIO()
        # self.source_block_stream = io.StringIO()
        # self.indent = 0
        self.print_function = False
        self.dependency_list = []
        self.namespace_path = []
        self.namespace_reference_path = []
        self.function_call_identifier = None
        self.function_arguments = []

    def exitHeaderBlock(self, ctx: creole_parser.HeaderBlockContext):
        for dependency in self.dependency_list:
            header = dependency.symbol.text.replace('"', '') + ".h"
            self.source_emitter.emit_top(f'#include <{header}>')

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
        self.source_emitter.emit(f'void {function_name}(void) {{')
        self.source_emitter.indent()
        self.print_function = False

    def exitFunction(self, ctx: creole_parser.FunctionContext):
        self.source_emitter.deindent()
        self.source_emitter.emit('}')

    def enterFunctionCall(self, ctx: creole_parser.FunctionCallContext):
        self.namespace_reference_path = []
        self.function_call_identifier = None
        self.function_arguments = []

    def exitFunctionCall(self, ctx: creole_parser.FunctionCallContext):
        if self.function_call_identifier.symbol.text == "print":
            self.source_emitter.emit_top('#include <stdio.h>')
            full_function_identifier = "printf"
        else:
            full_function_identifier = "_".join(
                map(lambda ident: ident.symbol.text, self.namespace_reference_path + [self.function_call_identifier])
            )
        function_arguments = ", ".join(
            map(lambda ident: ident.symbol.text, self.function_arguments)
        )

        self.source_emitter.emit(f'{full_function_identifier}({function_arguments});')

        if self.function_call_identifier.symbol.text == "print":
            self.source_emitter.emit(f'printf("\\n");')

    def enterNamespaceReferenceName(self, ctx: creole_parser.NamespaceReferenceNameContext):
        self.namespace_reference_path.append(ctx.children[0])

    def enterFunctionIdentifier(self, ctx: creole_parser.FunctionIdentifierContext):
        self.function_call_identifier = ctx.children[0]

    def enterFunctionArgument(self, ctx: creole_parser.FunctionArgumentContext):
        self.function_arguments.append(ctx.children[0])

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
        return self.header_emitter.value()

    def source_code(self):
        return self.source_emitter.value()
