# Generated from creole/creole_parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .creole_parser import creole_parser
else:
    from creole_parser import creole_parser

# This class defines a complete listener for a parse tree produced by creole_parser.
class creole_parserListener(ParseTreeListener):

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