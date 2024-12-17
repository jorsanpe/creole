parser grammar creole_parser;

options {
    tokenVocab = creole_lexer;
}

program
    : headerBlock block*;

headerBlock
    : IMPORT LBRACE dependencyList RBRACE
    |;

dependencyList
    : dependencyList COMMA StringLiteral
    | StringLiteral
    |;

block
    : function
    | namespace;

namespace
    : NAMESPACE Identifier LBRACE program RBRACE;

//class
//    :;
//
//test
//    :;

function
    : FUNCTION Identifier LPAREN RPAREN LBRACE statements RBRACE;

statements
    : statement*;

statement
    : functionCall;

functionCall
    : namespaceReference Identifier LPAREN functionArguments RPAREN SEMI;

namespaceReference
    : namespaceReference namespaceName DOUBLE_COLON
    | namespaceName DOUBLE_COLON
    |;

namespaceName
    : Identifier;

functionArguments
    : functionArgument
    | functionArgument (COMMA functionArgument)*
    |;

functionArgument
    : StringLiteral;
