LEXER_FILES := \
	creole/antlr/creole_lexer.py \
	creole/antlr/creole_lexer.tokens

PARSER_FILES := \
	creole/antlr/parser.py \
	creole/antlr/parser.tokens \
	creole/antlr/parserVisitor.py \
	creole/antlr/parserListener.py

build: $(LEXER_FILES) $(PARSER_FILES)

creole/antlr/creole_lexer.interp: creole/antlr/creole_lexer.g4
	antlr4 -Dlanguage=Python3 -visitor $^

$(LEXER_FILES): creole/antlr/creole_lexer.interp
	@: # Do nothing, the files are already created

creole/antlr/parser.interp: creole/antlr/creole_parser.g4
	antlr4 -Dlanguage=Python3 -visitor $^

$(PARSER_FILES): creole/antlr/parser.interp
	@: # Do nothing, the files are already created

parse:
	python creole/creole.py creole/samples/main.crl

test: build
	pytest-3

.PHONY: test