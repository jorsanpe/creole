parser grammar creole_parser;

options {
    tokenVocab = creole_lexer;
}

program
    : headerBlock? block*;

headerBlock
    : IMPORT LBRACE dependencyList? RBRACE;

dependencyList
    : dependencyList COMMA dependency
    | dependency;

dependency
    : StringLiteral;

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
    : namespaceReference? functionIdentifier LPAREN functionArguments? RPAREN SEMI;

namespaceReference
    : namespaceReference namespaceReferenceName DOUBLE_COLON
    | namespaceReferenceName DOUBLE_COLON;

functionIdentifier
    : Identifier;

namespaceReferenceName
    : Identifier;

functionArguments
    : functionArgument
    | functionArgument (COMMA functionArgument)*;

functionArgument
    : StringLiteral;
