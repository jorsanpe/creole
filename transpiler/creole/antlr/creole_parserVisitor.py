# Generated from creole/antlr/creole_parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .creole_parser import creole_parser
else:
    from creole_parser import creole_parser

# This class defines a complete generic visitor for a parse tree produced by creole_parser.

class creole_parserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by creole_parser#program.
    def visitProgram(self, ctx:creole_parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by creole_parser#block.
    def visitBlock(self, ctx:creole_parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by creole_parser#namespace.
    def visitNamespace(self, ctx:creole_parser.NamespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by creole_parser#function.
    def visitFunction(self, ctx:creole_parser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by creole_parser#statements.
    def visitStatements(self, ctx:creole_parser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by creole_parser#statement.
    def visitStatement(self, ctx:creole_parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by creole_parser#functionCall.
    def visitFunctionCall(self, ctx:creole_parser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by creole_parser#namespaceReference.
    def visitNamespaceReference(self, ctx:creole_parser.NamespaceReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by creole_parser#namespaceName.
    def visitNamespaceName(self, ctx:creole_parser.NamespaceNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by creole_parser#functionArguments.
    def visitFunctionArguments(self, ctx:creole_parser.FunctionArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by creole_parser#functionArgument.
    def visitFunctionArgument(self, ctx:creole_parser.FunctionArgumentContext):
        return self.visitChildren(ctx)



del creole_parser