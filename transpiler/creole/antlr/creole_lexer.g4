lexer grammar creole_lexer;

CLASS: 'class';
FUNCTION: 'fn';
NAMESPACE: 'namespace';
IMPORT: 'import';

IntegerLiteral:
    DecimalIntegerLiteral
    | HexIntegerLiteral
    | OctalIntegerLiteral
    | BinaryIntegerLiteral
;

fragment DecimalIntegerLiteral: DecimalNumeral IntegerTypeSuffix?;
fragment HexIntegerLiteral: HexNumeral IntegerTypeSuffix?;
fragment OctalIntegerLiteral: OctalNumeral IntegerTypeSuffix?;
fragment BinaryIntegerLiteral: BinaryNumeral IntegerTypeSuffix?;
fragment IntegerTypeSuffix: [lL];
fragment DecimalNumeral: '0' | NonZeroDigit (Digits? | Underscores Digits);
fragment Digits: Digit (DigitsAndUnderscores? Digit)?;
fragment Digit: '0' | NonZeroDigit;
fragment NonZeroDigit: [1-9];
fragment DigitsAndUnderscores: DigitOrUnderscore+;
fragment DigitOrUnderscore: Digit | '_';
fragment Underscores: '_'+;
fragment HexNumeral: '0' [xX] HexDigits;
fragment HexDigits: HexDigit (HexDigitsAndUnderscores? HexDigit)?;
fragment HexDigit: [0-9a-fA-F];
fragment HexDigitsAndUnderscores: HexDigitOrUnderscore+;
fragment HexDigitOrUnderscore: HexDigit | '_';
fragment OctalNumeral: '0' Underscores? OctalDigits;
fragment OctalDigits: OctalDigit (OctalDigitsAndUnderscores? OctalDigit)?;
fragment OctalDigit: [0-7];
fragment OctalDigitsAndUnderscores: OctalDigitOrUnderscore+;
fragment OctalDigitOrUnderscore: OctalDigit | '_';
fragment BinaryNumeral: '0' [bB] BinaryDigits;
fragment BinaryDigits: BinaryDigit (BinaryDigitsAndUnderscores? BinaryDigit)?;
fragment BinaryDigit: [01];
fragment BinaryDigitsAndUnderscores: BinaryDigitOrUnderscore+;
fragment BinaryDigitOrUnderscore: BinaryDigit | '_';

LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
ASSIGN: '=';
COMMA: ',';
DOUBLE_COLON: '::';

StringLiteral: '"' StringCharacters? '"';
fragment StringCharacters: StringCharacter+;
fragment StringCharacter: ~["\\\r\n];

Identifier
    : IdentifierNondigit (IdentifierNondigit | Digit)*
    ;

fragment IdentifierNondigit
    : Nondigit
    ;

fragment Nondigit
    : [a-zA-Z_]
    ;

Whitespace
    : [ \t]+ -> skip
    ;

Newline
    : ('\r' '\n'? | '\n') -> skip
    ;
