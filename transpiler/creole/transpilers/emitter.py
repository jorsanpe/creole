import io

INDENT = 4


class Emitter:
    def __init__(self):
        self.indent_level = 0
        self.top_stream = io.StringIO()
        self.mid_stream = io.StringIO()
        self.bottom_stream = io.StringIO()

    def value(self):
        return self.top_stream.getvalue() + self.mid_stream.getvalue() + self.bottom_stream.getvalue()

    def indent(self):
        self.indent_level += INDENT

    def deindent(self):
        self.indent_level -= INDENT

    def emit_top(self, code):
        self.top_stream.write(code)

    def emit_start(self, code):
        self.mid_stream.write(f'{" " * self.indent_level}{code}')

    def emit_end(self, code):
        self.mid_stream.write(code)
        self.mid_stream.write("\n")

    def emit_partial(self, code):
        self.mid_stream.write(code)

    def emit(self, code):
        self.mid_stream.write(f'{" " * self.indent_level}{code}\n')
