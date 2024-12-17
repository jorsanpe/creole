# Generated from creole/antlr/creole_parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .creole_parser import creole_parser
else:
    from creole_parser import creole_parser

# This class defines a complete listener for a parse tree produced by creole_parser.
class creole_parserListener(ParseTreeListener):

    # Enter a parse tree produced by creole_parser#program.
    def enterProgram(self, ctx:creole_parser.ProgramContext):
        pass

    # Exit a parse tree produced by creole_parser#program.
    def exitProgram(self, ctx:creole_parser.ProgramContext):
        pass


    # Enter a parse tree produced by creole_parser#headerBlock.
    def enterHeaderBlock(self, ctx:creole_parser.HeaderBlockContext):
        pass

    # Exit a parse tree produced by creole_parser#headerBlock.
    def exitHeaderBlock(self, ctx:creole_parser.HeaderBlockContext):
        pass


    # Enter a parse tree produced by creole_parser#dependencyList.
    def enterDependencyList(self, ctx:creole_parser.DependencyListContext):
        pass

    # Exit a parse tree produced by creole_parser#dependencyList.
    def exitDependencyList(self, ctx:creole_parser.DependencyListContext):
        pass


    # Enter a parse tree produced by creole_parser#dependency.
    def enterDependency(self, ctx:creole_parser.DependencyContext):
        pass

    # Exit a parse tree produced by creole_parser#dependency.
    def exitDependency(self, ctx:creole_parser.DependencyContext):
        pass


    # Enter a parse tree produced by creole_parser#block.
    def enterBlock(self, ctx:creole_parser.BlockContext):
        pass

    # Exit a parse tree produced by creole_parser#block.
    def exitBlock(self, ctx:creole_parser.BlockContext):
        pass


    # Enter a parse tree produced by creole_parser#namespace.
    def enterNamespace(self, ctx:creole_parser.NamespaceContext):
        pass

    # Exit a parse tree produced by creole_parser#namespace.
    def exitNamespace(self, ctx:creole_parser.NamespaceContext):
        pass


    # Enter a parse tree produced by creole_parser#function.
    def enterFunction(self, ctx:creole_parser.FunctionContext):
        pass

    # Exit a parse tree produced by creole_parser#function.
    def exitFunction(self, ctx:creole_parser.FunctionContext):
        pass


    # Enter a parse tree produced by creole_parser#statements.
    def enterStatements(self, ctx:creole_parser.StatementsContext):
        pass

    # Exit a parse tree produced by creole_parser#statements.
    def exitStatements(self, ctx:creole_parser.StatementsContext):
        pass


    # Enter a parse tree produced by creole_parser#statement.
    def enterStatement(self, ctx:creole_parser.StatementContext):
        pass

    # Exit a parse tree produced by creole_parser#statement.
    def exitStatement(self, ctx:creole_parser.StatementContext):
        pass


    # Enter a parse tree produced by creole_parser#functionCall.
    def enterFunctionCall(self, ctx:creole_parser.FunctionCallContext):
        pass

    # Exit a parse tree produced by creole_parser#functionCall.
    def exitFunctionCall(self, ctx:creole_parser.FunctionCallContext):
        pass


    # Enter a parse tree produced by creole_parser#namespaceReference.
    def enterNamespaceReference(self, ctx:creole_parser.NamespaceReferenceContext):
        pass

    # Exit a parse tree produced by creole_parser#namespaceReference.
    def exitNamespaceReference(self, ctx:creole_parser.NamespaceReferenceContext):
        pass


    # Enter a parse tree produced by creole_parser#namespaceName.
    def enterNamespaceName(self, ctx:creole_parser.NamespaceNameContext):
        pass

    # Exit a parse tree produced by creole_parser#namespaceName.
    def exitNamespaceName(self, ctx:creole_parser.NamespaceNameContext):
        pass


    # Enter a parse tree produced by creole_parser#functionArguments.
    def enterFunctionArguments(self, ctx:creole_parser.FunctionArgumentsContext):
        pass

    # Exit a parse tree produced by creole_parser#functionArguments.
    def exitFunctionArguments(self, ctx:creole_parser.FunctionArgumentsContext):
        pass


    # Enter a parse tree produced by creole_parser#functionArgument.
    def enterFunctionArgument(self, ctx:creole_parser.FunctionArgumentContext):
        pass

    # Exit a parse tree produced by creole_parser#functionArgument.
    def exitFunctionArgument(self, ctx:creole_parser.FunctionArgumentContext):
        pass



del creole_parser