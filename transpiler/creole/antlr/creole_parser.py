# Generated from creole/antlr/creole_parser.g4 by ANTLR 4.13.2
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
        4,1,16,88,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,5,0,24,8,0,10,0,12,0,27,
        9,0,1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,4,5,4,48,8,4,10,4,12,4,51,9,4,1,5,1,5,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,70,8,7,1,8,
        1,8,1,9,1,9,1,9,1,9,5,9,78,8,9,10,9,12,9,81,9,9,1,9,3,9,84,8,9,1,
        10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,0,84,0,25,1,0,
        0,0,2,30,1,0,0,0,4,32,1,0,0,0,6,38,1,0,0,0,8,49,1,0,0,0,10,52,1,
        0,0,0,12,54,1,0,0,0,14,69,1,0,0,0,16,71,1,0,0,0,18,83,1,0,0,0,20,
        85,1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,
        0,25,26,1,0,0,0,26,1,1,0,0,0,27,25,1,0,0,0,28,31,3,6,3,0,29,31,3,
        4,2,0,30,28,1,0,0,0,30,29,1,0,0,0,31,3,1,0,0,0,32,33,5,3,0,0,33,
        34,5,14,0,0,34,35,5,7,0,0,35,36,3,0,0,0,36,37,5,8,0,0,37,5,1,0,0,
        0,38,39,5,2,0,0,39,40,5,14,0,0,40,41,5,5,0,0,41,42,5,6,0,0,42,43,
        5,7,0,0,43,44,3,8,4,0,44,45,5,8,0,0,45,7,1,0,0,0,46,48,3,10,5,0,
        47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,9,1,0,
        0,0,51,49,1,0,0,0,52,53,3,12,6,0,53,11,1,0,0,0,54,55,3,14,7,0,55,
        56,5,14,0,0,56,57,5,5,0,0,57,58,3,18,9,0,58,59,5,6,0,0,59,60,5,9,
        0,0,60,13,1,0,0,0,61,62,3,16,8,0,62,63,5,12,0,0,63,64,3,14,7,0,64,
        70,1,0,0,0,65,66,3,16,8,0,66,67,5,12,0,0,67,70,1,0,0,0,68,70,1,0,
        0,0,69,61,1,0,0,0,69,65,1,0,0,0,69,68,1,0,0,0,70,15,1,0,0,0,71,72,
        5,14,0,0,72,17,1,0,0,0,73,84,3,20,10,0,74,79,3,20,10,0,75,76,5,11,
        0,0,76,78,3,20,10,0,77,75,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,
        80,1,0,0,0,80,84,1,0,0,0,81,79,1,0,0,0,82,84,1,0,0,0,83,73,1,0,0,
        0,83,74,1,0,0,0,83,82,1,0,0,0,84,19,1,0,0,0,85,86,5,13,0,0,86,21,
        1,0,0,0,6,25,30,49,69,79,83
    ]

class creole_parser ( Parser ):

    grammarFileName = "creole_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'fn'", "'namespace'", "<INVALID>", 
                     "'('", "')'", "'{'", "'}'", "';'", "'='", "','", "'::'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "FUNCTION", "NAMESPACE", "IntegerLiteral", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "SEMI", "ASSIGN", 
                      "COMMA", "DOUBLE_COLON", "StringLiteral", "Identifier", 
                      "Whitespace", "Newline" ]

    RULE_program = 0
    RULE_block = 1
    RULE_namespace = 2
    RULE_function = 3
    RULE_statements = 4
    RULE_statement = 5
    RULE_functionCall = 6
    RULE_namespaceReference = 7
    RULE_namespaceName = 8
    RULE_functionArguments = 9
    RULE_functionArgument = 10

    ruleNames =  [ "program", "block", "namespace", "function", "statements", 
                   "statement", "functionCall", "namespaceReference", "namespaceName", 
                   "functionArguments", "functionArgument" ]

    EOF = Token.EOF
    CLASS=1
    FUNCTION=2
    NAMESPACE=3
    IntegerLiteral=4
    LPAREN=5
    RPAREN=6
    LBRACE=7
    RBRACE=8
    SEMI=9
    ASSIGN=10
    COMMA=11
    DOUBLE_COLON=12
    StringLiteral=13
    Identifier=14
    Whitespace=15
    Newline=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(creole_parser.BlockContext)
            else:
                return self.getTypedRuleContext(creole_parser.BlockContext,i)


        def getRuleIndex(self):
            return creole_parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = creole_parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==3:
                self.state = 22
                self.block()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(creole_parser.FunctionContext,0)


        def namespace(self):
            return self.getTypedRuleContext(creole_parser.NamespaceContext,0)


        def getRuleIndex(self):
            return creole_parser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = creole_parser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.function()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.namespace()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamespaceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAMESPACE(self):
            return self.getToken(creole_parser.NAMESPACE, 0)

        def Identifier(self):
            return self.getToken(creole_parser.Identifier, 0)

        def LBRACE(self):
            return self.getToken(creole_parser.LBRACE, 0)

        def program(self):
            return self.getTypedRuleContext(creole_parser.ProgramContext,0)


        def RBRACE(self):
            return self.getToken(creole_parser.RBRACE, 0)

        def getRuleIndex(self):
            return creole_parser.RULE_namespace

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespace" ):
                listener.enterNamespace(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespace" ):
                listener.exitNamespace(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamespace" ):
                return visitor.visitNamespace(self)
            else:
                return visitor.visitChildren(self)




    def namespace(self):

        localctx = creole_parser.NamespaceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_namespace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(creole_parser.NAMESPACE)
            self.state = 33
            self.match(creole_parser.Identifier)
            self.state = 34
            self.match(creole_parser.LBRACE)
            self.state = 35
            self.program()
            self.state = 36
            self.match(creole_parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


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
        self.enterRule(localctx, 6, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(creole_parser.FUNCTION)
            self.state = 39
            self.match(creole_parser.Identifier)
            self.state = 40
            self.match(creole_parser.LPAREN)
            self.state = 41
            self.match(creole_parser.RPAREN)
            self.state = 42
            self.match(creole_parser.LBRACE)
            self.state = 43
            self.statements()
            self.state = 44
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
        self.enterRule(localctx, 8, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 46
                self.statement()
                self.state = 51
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
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
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

        def namespaceReference(self):
            return self.getTypedRuleContext(creole_parser.NamespaceReferenceContext,0)


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
        self.enterRule(localctx, 12, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.namespaceReference()
            self.state = 55
            self.match(creole_parser.Identifier)
            self.state = 56
            self.match(creole_parser.LPAREN)
            self.state = 57
            self.functionArguments()
            self.state = 58
            self.match(creole_parser.RPAREN)
            self.state = 59
            self.match(creole_parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamespaceReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namespaceName(self):
            return self.getTypedRuleContext(creole_parser.NamespaceNameContext,0)


        def DOUBLE_COLON(self):
            return self.getToken(creole_parser.DOUBLE_COLON, 0)

        def namespaceReference(self):
            return self.getTypedRuleContext(creole_parser.NamespaceReferenceContext,0)


        def getRuleIndex(self):
            return creole_parser.RULE_namespaceReference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespaceReference" ):
                listener.enterNamespaceReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespaceReference" ):
                listener.exitNamespaceReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamespaceReference" ):
                return visitor.visitNamespaceReference(self)
            else:
                return visitor.visitChildren(self)




    def namespaceReference(self):

        localctx = creole_parser.NamespaceReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_namespaceReference)
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.namespaceName()
                self.state = 62
                self.match(creole_parser.DOUBLE_COLON)
                self.state = 63
                self.namespaceReference()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.namespaceName()
                self.state = 66
                self.match(creole_parser.DOUBLE_COLON)
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


    class NamespaceNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(creole_parser.Identifier, 0)

        def getRuleIndex(self):
            return creole_parser.RULE_namespaceName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespaceName" ):
                listener.enterNamespaceName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespaceName" ):
                listener.exitNamespaceName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamespaceName" ):
                return visitor.visitNamespaceName(self)
            else:
                return visitor.visitChildren(self)




    def namespaceName(self):

        localctx = creole_parser.NamespaceNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_namespaceName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(creole_parser.Identifier)
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
        self.enterRule(localctx, 18, self.RULE_functionArguments)
        self._la = 0 # Token type
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.functionArgument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.functionArgument()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11:
                    self.state = 75
                    self.match(creole_parser.COMMA)
                    self.state = 76
                    self.functionArgument()
                    self.state = 81
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
        self.enterRule(localctx, 20, self.RULE_functionArgument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(creole_parser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





