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
        4,1,17,127,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,3,0,32,8,0,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,1,1,1,
        1,1,3,1,43,8,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,5,2,53,8,2,10,2,12,
        2,56,9,2,1,3,1,3,1,4,1,4,3,4,62,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,5,7,79,8,7,10,7,12,7,82,9,7,1,8,
        1,8,1,9,3,9,87,8,9,1,9,1,9,1,9,3,9,92,8,9,1,9,1,9,1,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,5,10,105,8,10,10,10,12,10,108,9,10,
        1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,13,5,13,118,8,13,10,13,12,13,
        121,9,13,3,13,123,8,13,1,14,1,14,1,14,0,2,4,20,15,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,0,0,122,0,31,1,0,0,0,2,39,1,0,0,0,4,46,1,
        0,0,0,6,57,1,0,0,0,8,61,1,0,0,0,10,63,1,0,0,0,12,69,1,0,0,0,14,80,
        1,0,0,0,16,83,1,0,0,0,18,86,1,0,0,0,20,96,1,0,0,0,22,109,1,0,0,0,
        24,111,1,0,0,0,26,122,1,0,0,0,28,124,1,0,0,0,30,32,3,2,1,0,31,30,
        1,0,0,0,31,32,1,0,0,0,32,36,1,0,0,0,33,35,3,8,4,0,34,33,1,0,0,0,
        35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,1,1,0,0,0,38,36,1,0,
        0,0,39,40,5,4,0,0,40,42,5,8,0,0,41,43,3,4,2,0,42,41,1,0,0,0,42,43,
        1,0,0,0,43,44,1,0,0,0,44,45,5,9,0,0,45,3,1,0,0,0,46,47,6,2,-1,0,
        47,48,3,6,3,0,48,54,1,0,0,0,49,50,10,2,0,0,50,51,5,12,0,0,51,53,
        3,6,3,0,52,49,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,
        55,5,1,0,0,0,56,54,1,0,0,0,57,58,5,14,0,0,58,7,1,0,0,0,59,62,3,12,
        6,0,60,62,3,10,5,0,61,59,1,0,0,0,61,60,1,0,0,0,62,9,1,0,0,0,63,64,
        5,3,0,0,64,65,5,15,0,0,65,66,5,8,0,0,66,67,3,0,0,0,67,68,5,9,0,0,
        68,11,1,0,0,0,69,70,5,2,0,0,70,71,5,15,0,0,71,72,5,6,0,0,72,73,5,
        7,0,0,73,74,5,8,0,0,74,75,3,14,7,0,75,76,5,9,0,0,76,13,1,0,0,0,77,
        79,3,16,8,0,78,77,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,
        0,0,81,15,1,0,0,0,82,80,1,0,0,0,83,84,3,18,9,0,84,17,1,0,0,0,85,
        87,3,20,10,0,86,85,1,0,0,0,86,87,1,0,0,0,87,88,1,0,0,0,88,89,3,22,
        11,0,89,91,5,6,0,0,90,92,3,26,13,0,91,90,1,0,0,0,91,92,1,0,0,0,92,
        93,1,0,0,0,93,94,5,7,0,0,94,95,5,10,0,0,95,19,1,0,0,0,96,97,6,10,
        -1,0,97,98,3,24,12,0,98,99,5,13,0,0,99,106,1,0,0,0,100,101,10,2,
        0,0,101,102,3,24,12,0,102,103,5,13,0,0,103,105,1,0,0,0,104,100,1,
        0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,107,1,0,0,0,107,21,1,0,
        0,0,108,106,1,0,0,0,109,110,5,15,0,0,110,23,1,0,0,0,111,112,5,15,
        0,0,112,25,1,0,0,0,113,123,3,28,14,0,114,119,3,28,14,0,115,116,5,
        12,0,0,116,118,3,28,14,0,117,115,1,0,0,0,118,121,1,0,0,0,119,117,
        1,0,0,0,119,120,1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,122,113,
        1,0,0,0,122,114,1,0,0,0,123,27,1,0,0,0,124,125,5,14,0,0,125,29,1,
        0,0,0,11,31,36,42,54,61,80,86,91,106,119,122
    ]

class creole_parser ( Parser ):

    grammarFileName = "creole_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'fn'", "'namespace'", "'import'", 
                     "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'='", 
                     "','", "'::'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "FUNCTION", "NAMESPACE", "IMPORT", 
                      "IntegerLiteral", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "SEMI", "ASSIGN", "COMMA", "DOUBLE_COLON", "StringLiteral", 
                      "Identifier", "Whitespace", "Newline" ]

    RULE_program = 0
    RULE_headerBlock = 1
    RULE_dependencyList = 2
    RULE_dependency = 3
    RULE_block = 4
    RULE_namespace = 5
    RULE_function = 6
    RULE_statements = 7
    RULE_statement = 8
    RULE_functionCall = 9
    RULE_namespaceReference = 10
    RULE_functionIdentifier = 11
    RULE_namespaceReferenceName = 12
    RULE_functionArguments = 13
    RULE_functionArgument = 14

    ruleNames =  [ "program", "headerBlock", "dependencyList", "dependency", 
                   "block", "namespace", "function", "statements", "statement", 
                   "functionCall", "namespaceReference", "functionIdentifier", 
                   "namespaceReferenceName", "functionArguments", "functionArgument" ]

    EOF = Token.EOF
    CLASS=1
    FUNCTION=2
    NAMESPACE=3
    IMPORT=4
    IntegerLiteral=5
    LPAREN=6
    RPAREN=7
    LBRACE=8
    RBRACE=9
    SEMI=10
    ASSIGN=11
    COMMA=12
    DOUBLE_COLON=13
    StringLiteral=14
    Identifier=15
    Whitespace=16
    Newline=17

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

        def headerBlock(self):
            return self.getTypedRuleContext(creole_parser.HeaderBlockContext,0)


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
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 30
                self.headerBlock()


            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==3:
                self.state = 33
                self.block()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeaderBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(creole_parser.IMPORT, 0)

        def LBRACE(self):
            return self.getToken(creole_parser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(creole_parser.RBRACE, 0)

        def dependencyList(self):
            return self.getTypedRuleContext(creole_parser.DependencyListContext,0)


        def getRuleIndex(self):
            return creole_parser.RULE_headerBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeaderBlock" ):
                listener.enterHeaderBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeaderBlock" ):
                listener.exitHeaderBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeaderBlock" ):
                return visitor.visitHeaderBlock(self)
            else:
                return visitor.visitChildren(self)




    def headerBlock(self):

        localctx = creole_parser.HeaderBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_headerBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(creole_parser.IMPORT)
            self.state = 40
            self.match(creole_parser.LBRACE)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 41
                self.dependencyList(0)


            self.state = 44
            self.match(creole_parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DependencyListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dependency(self):
            return self.getTypedRuleContext(creole_parser.DependencyContext,0)


        def dependencyList(self):
            return self.getTypedRuleContext(creole_parser.DependencyListContext,0)


        def COMMA(self):
            return self.getToken(creole_parser.COMMA, 0)

        def getRuleIndex(self):
            return creole_parser.RULE_dependencyList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDependencyList" ):
                listener.enterDependencyList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDependencyList" ):
                listener.exitDependencyList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDependencyList" ):
                return visitor.visitDependencyList(self)
            else:
                return visitor.visitChildren(self)



    def dependencyList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = creole_parser.DependencyListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_dependencyList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.dependency()
            self._ctx.stop = self._input.LT(-1)
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = creole_parser.DependencyListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_dependencyList)
                    self.state = 49
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 50
                    self.match(creole_parser.COMMA)
                    self.state = 51
                    self.dependency() 
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DependencyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def StringLiteral(self):
            return self.getToken(creole_parser.StringLiteral, 0)

        def getRuleIndex(self):
            return creole_parser.RULE_dependency

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDependency" ):
                listener.enterDependency(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDependency" ):
                listener.exitDependency(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDependency" ):
                return visitor.visitDependency(self)
            else:
                return visitor.visitChildren(self)




    def dependency(self):

        localctx = creole_parser.DependencyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_dependency)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(creole_parser.StringLiteral)
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
        self.enterRule(localctx, 8, self.RULE_block)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.function()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
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
        self.enterRule(localctx, 10, self.RULE_namespace)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(creole_parser.NAMESPACE)
            self.state = 64
            self.match(creole_parser.Identifier)
            self.state = 65
            self.match(creole_parser.LBRACE)
            self.state = 66
            self.program()
            self.state = 67
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
        self.enterRule(localctx, 12, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(creole_parser.FUNCTION)
            self.state = 70
            self.match(creole_parser.Identifier)
            self.state = 71
            self.match(creole_parser.LPAREN)
            self.state = 72
            self.match(creole_parser.RPAREN)
            self.state = 73
            self.match(creole_parser.LBRACE)
            self.state = 74
            self.statements()
            self.state = 75
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
        self.enterRule(localctx, 14, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 77
                self.statement()
                self.state = 82
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
        self.enterRule(localctx, 16, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
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

        def functionIdentifier(self):
            return self.getTypedRuleContext(creole_parser.FunctionIdentifierContext,0)


        def LPAREN(self):
            return self.getToken(creole_parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(creole_parser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(creole_parser.SEMI, 0)

        def namespaceReference(self):
            return self.getTypedRuleContext(creole_parser.NamespaceReferenceContext,0)


        def functionArguments(self):
            return self.getTypedRuleContext(creole_parser.FunctionArgumentsContext,0)


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
        self.enterRule(localctx, 18, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 85
                self.namespaceReference(0)


            self.state = 88
            self.functionIdentifier()
            self.state = 89
            self.match(creole_parser.LPAREN)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 90
                self.functionArguments()


            self.state = 93
            self.match(creole_parser.RPAREN)
            self.state = 94
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

        def namespaceReferenceName(self):
            return self.getTypedRuleContext(creole_parser.NamespaceReferenceNameContext,0)


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



    def namespaceReference(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = creole_parser.NamespaceReferenceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_namespaceReference, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.namespaceReferenceName()
            self.state = 98
            self.match(creole_parser.DOUBLE_COLON)
            self._ctx.stop = self._input.LT(-1)
            self.state = 106
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = creole_parser.NamespaceReferenceContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_namespaceReference)
                    self.state = 100
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 101
                    self.namespaceReferenceName()
                    self.state = 102
                    self.match(creole_parser.DOUBLE_COLON) 
                self.state = 108
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(creole_parser.Identifier, 0)

        def getRuleIndex(self):
            return creole_parser.RULE_functionIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionIdentifier" ):
                listener.enterFunctionIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionIdentifier" ):
                listener.exitFunctionIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionIdentifier" ):
                return visitor.visitFunctionIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def functionIdentifier(self):

        localctx = creole_parser.FunctionIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_functionIdentifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(creole_parser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamespaceReferenceNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(creole_parser.Identifier, 0)

        def getRuleIndex(self):
            return creole_parser.RULE_namespaceReferenceName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamespaceReferenceName" ):
                listener.enterNamespaceReferenceName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamespaceReferenceName" ):
                listener.exitNamespaceReferenceName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamespaceReferenceName" ):
                return visitor.visitNamespaceReferenceName(self)
            else:
                return visitor.visitChildren(self)




    def namespaceReferenceName(self):

        localctx = creole_parser.NamespaceReferenceNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_namespaceReferenceName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
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
        self.enterRule(localctx, 26, self.RULE_functionArguments)
        self._la = 0 # Token type
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.functionArgument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.functionArgument()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 115
                    self.match(creole_parser.COMMA)
                    self.state = 116
                    self.functionArgument()
                    self.state = 121
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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
        self.enterRule(localctx, 28, self.RULE_functionArgument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(creole_parser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.dependencyList_sempred
        self._predicates[10] = self.namespaceReference_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def dependencyList_sempred(self, localctx:DependencyListContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def namespaceReference_sempred(self, localctx:NamespaceReferenceContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




