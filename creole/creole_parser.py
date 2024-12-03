# Generated from creole/creole_parser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,49,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,5,1,22,8,1,10,1,12,1,25,9,1,1,2,1,
        2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,5,4,39,8,4,10,4,12,4,42,
        9,4,1,4,3,4,45,8,4,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,0,46,0,12,1,
        0,0,0,2,23,1,0,0,0,4,26,1,0,0,0,6,28,1,0,0,0,8,44,1,0,0,0,10,46,
        1,0,0,0,12,13,5,2,0,0,13,14,5,12,0,0,14,15,5,4,0,0,15,16,5,5,0,0,
        16,17,5,6,0,0,17,18,3,2,1,0,18,19,5,7,0,0,19,1,1,0,0,0,20,22,3,4,
        2,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,3,
        1,0,0,0,25,23,1,0,0,0,26,27,3,6,3,0,27,5,1,0,0,0,28,29,5,12,0,0,
        29,30,5,4,0,0,30,31,3,8,4,0,31,32,5,5,0,0,32,33,5,8,0,0,33,7,1,0,
        0,0,34,45,3,10,5,0,35,40,3,10,5,0,36,37,5,10,0,0,37,39,3,10,5,0,
        38,36,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,45,1,
        0,0,0,42,40,1,0,0,0,43,45,1,0,0,0,44,34,1,0,0,0,44,35,1,0,0,0,44,
        43,1,0,0,0,45,9,1,0,0,0,46,47,5,11,0,0,47,11,1,0,0,0,3,23,40,44
    ]

class creole_parser ( Parser ):

    grammarFileName = "creole_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'fn'", "<INVALID>", "'('", 
                     "')'", "'{'", "'}'", "';'", "'='", "','" ]

    symbolicNames = [ "<INVALID>", "CLASS", "FUNCTION", "IntegerLiteral", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "SEMI", "ASSIGN", 
                      "COMMA", "StringLiteral", "Identifier", "Whitespace", 
                      "Newline" ]

    RULE_function = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_functionCall = 3
    RULE_functionArguments = 4
    RULE_functionArgument = 5

    ruleNames =  [ "function", "statements", "statement", "functionCall", 
                   "functionArguments", "functionArgument" ]

    EOF = Token.EOF
    CLASS=1
    FUNCTION=2
    IntegerLiteral=3
    LPAREN=4
    RPAREN=5
    LBRACE=6
    RBRACE=7
    SEMI=8
    ASSIGN=9
    COMMA=10
    StringLiteral=11
    Identifier=12
    Whitespace=13
    Newline=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(creole_parser.FUNCTION, 0)

        def Identifier(self):
            return self.getToken(creole_parser.Identifier, 0)

        def LPAREN(self):
            return self.getToken(creole_parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(creole_parser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(creole_parser.LBRACE, 0)

        def statements(self):
            return self.getTypedRuleContext(creole_parser.StatementsContext,0)


        def RBRACE(self):
            return self.getToken(creole_parser.RBRACE, 0)

        def getRuleIndex(self):
            return creole_parser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = creole_parser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(creole_parser.FUNCTION)
            self.state = 13
            self.match(creole_parser.Identifier)
            self.state = 14
            self.match(creole_parser.LPAREN)
            self.state = 15
            self.match(creole_parser.RPAREN)
            self.state = 16
            self.match(creole_parser.LBRACE)
            self.state = 17
            self.statements()
            self.state = 18
            self.match(creole_parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(creole_parser.StatementContext)
            else:
                return self.getTypedRuleContext(creole_parser.StatementContext,i)


        def getRuleIndex(self):
            return creole_parser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = creole_parser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 20
                self.statement()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(creole_parser.FunctionCallContext,0)


        def getRuleIndex(self):
            return creole_parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = creole_parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.functionCall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(creole_parser.Identifier, 0)

        def LPAREN(self):
            return self.getToken(creole_parser.LPAREN, 0)

        def functionArguments(self):
            return self.getTypedRuleContext(creole_parser.FunctionArgumentsContext,0)


        def RPAREN(self):
            return self.getToken(creole_parser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(creole_parser.SEMI, 0)

        def getRuleIndex(self):
            return creole_parser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = creole_parser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(creole_parser.Identifier)
            self.state = 29
            self.match(creole_parser.LPAREN)
            self.state = 30
            self.functionArguments()
            self.state = 31
            self.match(creole_parser.RPAREN)
            self.state = 32
            self.match(creole_parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionArgument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(creole_parser.FunctionArgumentContext)
            else:
                return self.getTypedRuleContext(creole_parser.FunctionArgumentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(creole_parser.COMMA)
            else:
                return self.getToken(creole_parser.COMMA, i)

        def getRuleIndex(self):
            return creole_parser.RULE_functionArguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionArguments" ):
                listener.enterFunctionArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionArguments" ):
                listener.exitFunctionArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionArguments" ):
                return visitor.visitFunctionArguments(self)
            else:
                return visitor.visitChildren(self)




    def functionArguments(self):

        localctx = creole_parser.FunctionArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionArguments)
        self._la = 0 # Token type
        try:
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.functionArgument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.functionArgument()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 36
                    self.match(creole_parser.COMMA)
                    self.state = 37
                    self.functionArgument()
                    self.state = 42
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def StringLiteral(self):
            return self.getToken(creole_parser.StringLiteral, 0)

        def getRuleIndex(self):
            return creole_parser.RULE_functionArgument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionArgument" ):
                listener.enterFunctionArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionArgument" ):
                listener.exitFunctionArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionArgument" ):
                return visitor.visitFunctionArgument(self)
            else:
                return visitor.visitChildren(self)




    def functionArgument(self):

        localctx = creole_parser.FunctionArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionArgument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(creole_parser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





