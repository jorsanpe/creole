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
        4,1,17,123,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,3,0,30,8,0,1,0,5,0,33,8,0,10,0,12,0,36,9,0,1,1,1,1,1,1,3,1,41,
        8,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,5,2,51,8,2,10,2,12,2,54,9,2,
        1,3,1,3,1,4,1,4,3,4,60,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,7,5,7,77,8,7,10,7,12,7,80,9,7,1,8,1,8,1,9,3,
        9,85,8,9,1,9,1,9,1,9,3,9,90,8,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,5,10,103,8,10,10,10,12,10,106,9,10,1,11,1,11,
        1,12,1,12,1,12,1,12,5,12,114,8,12,10,12,12,12,117,9,12,3,12,119,
        8,12,1,13,1,13,1,13,0,2,4,20,14,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,0,0,119,0,29,1,0,0,0,2,37,1,0,0,0,4,44,1,0,0,0,6,55,1,0,0,0,8,
        59,1,0,0,0,10,61,1,0,0,0,12,67,1,0,0,0,14,78,1,0,0,0,16,81,1,0,0,
        0,18,84,1,0,0,0,20,94,1,0,0,0,22,107,1,0,0,0,24,118,1,0,0,0,26,120,
        1,0,0,0,28,30,3,2,1,0,29,28,1,0,0,0,29,30,1,0,0,0,30,34,1,0,0,0,
        31,33,3,8,4,0,32,31,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,1,
        0,0,0,35,1,1,0,0,0,36,34,1,0,0,0,37,38,5,4,0,0,38,40,5,8,0,0,39,
        41,3,4,2,0,40,39,1,0,0,0,40,41,1,0,0,0,41,42,1,0,0,0,42,43,5,9,0,
        0,43,3,1,0,0,0,44,45,6,2,-1,0,45,46,3,6,3,0,46,52,1,0,0,0,47,48,
        10,2,0,0,48,49,5,12,0,0,49,51,3,6,3,0,50,47,1,0,0,0,51,54,1,0,0,
        0,52,50,1,0,0,0,52,53,1,0,0,0,53,5,1,0,0,0,54,52,1,0,0,0,55,56,5,
        14,0,0,56,7,1,0,0,0,57,60,3,12,6,0,58,60,3,10,5,0,59,57,1,0,0,0,
        59,58,1,0,0,0,60,9,1,0,0,0,61,62,5,3,0,0,62,63,5,15,0,0,63,64,5,
        8,0,0,64,65,3,0,0,0,65,66,5,9,0,0,66,11,1,0,0,0,67,68,5,2,0,0,68,
        69,5,15,0,0,69,70,5,6,0,0,70,71,5,7,0,0,71,72,5,8,0,0,72,73,3,14,
        7,0,73,74,5,9,0,0,74,13,1,0,0,0,75,77,3,16,8,0,76,75,1,0,0,0,77,
        80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,15,1,0,0,0,80,78,1,0,0,
        0,81,82,3,18,9,0,82,17,1,0,0,0,83,85,3,20,10,0,84,83,1,0,0,0,84,
        85,1,0,0,0,85,86,1,0,0,0,86,87,5,15,0,0,87,89,5,6,0,0,88,90,3,24,
        12,0,89,88,1,0,0,0,89,90,1,0,0,0,90,91,1,0,0,0,91,92,5,7,0,0,92,
        93,5,10,0,0,93,19,1,0,0,0,94,95,6,10,-1,0,95,96,3,22,11,0,96,97,
        5,13,0,0,97,104,1,0,0,0,98,99,10,2,0,0,99,100,3,22,11,0,100,101,
        5,13,0,0,101,103,1,0,0,0,102,98,1,0,0,0,103,106,1,0,0,0,104,102,
        1,0,0,0,104,105,1,0,0,0,105,21,1,0,0,0,106,104,1,0,0,0,107,108,5,
        15,0,0,108,23,1,0,0,0,109,119,3,26,13,0,110,115,3,26,13,0,111,112,
        5,12,0,0,112,114,3,26,13,0,113,111,1,0,0,0,114,117,1,0,0,0,115,113,
        1,0,0,0,115,116,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,118,109,
        1,0,0,0,118,110,1,0,0,0,119,25,1,0,0,0,120,121,5,14,0,0,121,27,1,
        0,0,0,11,29,34,40,52,59,78,84,89,104,115,118
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
    RULE_namespaceName = 11
    RULE_functionArguments = 12
    RULE_functionArgument = 13

    ruleNames =  [ "program", "headerBlock", "dependencyList", "dependency", 
                   "block", "namespace", "function", "statements", "statement", 
                   "functionCall", "namespaceReference", "namespaceName", 
                   "functionArguments", "functionArgument" ]

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
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 28
                self.headerBlock()


            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==3:
                self.state = 31
                self.block()
                self.state = 36
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
            self.state = 37
            self.match(creole_parser.IMPORT)
            self.state = 38
            self.match(creole_parser.LBRACE)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 39
                self.dependencyList(0)


            self.state = 42
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
            self.state = 45
            self.dependency()
            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = creole_parser.DependencyListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_dependencyList)
                    self.state = 47
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 48
                    self.match(creole_parser.COMMA)
                    self.state = 49
                    self.dependency() 
                self.state = 54
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
            self.state = 55
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
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.function()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
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
            self.state = 61
            self.match(creole_parser.NAMESPACE)
            self.state = 62
            self.match(creole_parser.Identifier)
            self.state = 63
            self.match(creole_parser.LBRACE)
            self.state = 64
            self.program()
            self.state = 65
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
            self.state = 67
            self.match(creole_parser.FUNCTION)
            self.state = 68
            self.match(creole_parser.Identifier)
            self.state = 69
            self.match(creole_parser.LPAREN)
            self.state = 70
            self.match(creole_parser.RPAREN)
            self.state = 71
            self.match(creole_parser.LBRACE)
            self.state = 72
            self.statements()
            self.state = 73
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
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 75
                self.statement()
                self.state = 80
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
            self.state = 81
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
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 83
                self.namespaceReference(0)


            self.state = 86
            self.match(creole_parser.Identifier)
            self.state = 87
            self.match(creole_parser.LPAREN)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 88
                self.functionArguments()


            self.state = 91
            self.match(creole_parser.RPAREN)
            self.state = 92
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



    def namespaceReference(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = creole_parser.NamespaceReferenceContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_namespaceReference, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.namespaceName()
            self.state = 96
            self.match(creole_parser.DOUBLE_COLON)
            self._ctx.stop = self._input.LT(-1)
            self.state = 104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = creole_parser.NamespaceReferenceContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_namespaceReference)
                    self.state = 98
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 99
                    self.namespaceName()
                    self.state = 100
                    self.match(creole_parser.DOUBLE_COLON) 
                self.state = 106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 22, self.RULE_namespaceName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
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
        self.enterRule(localctx, 24, self.RULE_functionArguments)
        self._la = 0 # Token type
        try:
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.functionArgument()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.functionArgument()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 111
                    self.match(creole_parser.COMMA)
                    self.state = 112
                    self.functionArgument()
                    self.state = 117
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
        self.enterRule(localctx, 26, self.RULE_functionArgument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
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
         




