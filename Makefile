generate:
	antlr4 -Dlanguage=Python3 -visitor creole/creole_lexer.g4
	antlr4 -Dlanguage=Python3 -visitor creole/creole_parser.g4

parse:
	python creole/creole.py creole/samples/main.crl

test:
	pytest-3

.PHONY: test