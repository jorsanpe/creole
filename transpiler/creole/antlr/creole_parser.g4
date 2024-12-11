parser grammar creole_parser;

options {
    tokenVocab = creole_lexer;
}

function
    : FUNCTION Identifier LPAREN RPAREN LBRACE statements RBRACE;

statements
    : statement*;

statement
    : functionCall;

functionCall
    : Identifier LPAREN functionArguments RPAREN SEMI;

functionArguments
    : functionArgument
    | functionArgument (COMMA functionArgument)*
    |;

functionArgument
    : StringLiteral;
