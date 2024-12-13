parser grammar creole_parser;

options {
    tokenVocab = creole_lexer;
}

program
    : block*;

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
    : namespaceName DOUBLE_COLON namespaceReference
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
