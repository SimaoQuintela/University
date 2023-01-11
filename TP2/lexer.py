import ply.lex as lex
import sys

tokens = (
    'INTDec',
    'NUM',
    'ID',
    'ATRIB',
    'EQUIV',
    'LEQ',  # <= - (less or equal)
    'GEQ',  # >= - (greater or equal)
    'GT',   # >  - (greater than)
    'LT',   # <  - (less than)
    'IF',
    'ELSE',
    'ELIF',
    'LCPARENT',
    'RCPARENT',
    'LSQBRACKET', # left square bracket
    'RSQBRACKET', # right square bracket
    'AND',
    'OR',
    'SUM',
    'SUB',
    'DIV',
    'MULT',
    'MOD',
    'INC',
    'DEC',
    'DO',
    'WHILE',
    'PRINT',
    'QUOTE', # Símbolo "
    'STRING',
    'INPUT',
    'NEWLINE',
    'WS',
    'COLON',
    'INDENT',
    'DEDENT',
    'ENDMARKER'
)

literals = [',']


def t_WS(t):
    r'[ ]+'
    t.type = "WS"
    if t.lexer.at_line_start and t.lexer.paren_count == 0:
        return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    t.type = "NEWLINE"
    if t.lexer.paren_count == 0:
        return t

def t_COLON(t):
    r':'
    return t

def t_QUOTE(t):
    r'\"'
    return t

# returns the content inside quotes
def t_STRING(t):
    r'(?<=\")[A-Za-z0-9\, \?\-\:\\]*(?=\")'
    return t

def t_INPUT(t):
    r'input'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_MOD(t):
    r'\%'
    return t

def t_INC(t):
    r'\+\+'
    return t

def t_DEC(t):
    r'\-\-'
    return t

def t_SUM(t):
    r'\+'
    return t

def t_SUB(t):
    r'\-'
    return t

def t_DIV(t):
    r'\/'
    return t

def t_MULT(t):
    r'\*'
    return t

def t_LSQBRACKET(t):
    r'\['
    return t

def t_RSQBRACKET(t):
    r'\]'
    return t

def t_LEQ(t):
    r'\<\='
    return t

def t_GEQ(t):
    r'\>\='
    return t

def t_GT(t):
    r'\>'
    return t

def t_LT(t):
    r'\<'
    return t

# (?= ) - lookahead, looks for a white space after de int keyword
#  cover the cases:
#    - int x       
#    - intare x
# without the lookahead both would be considered INT tokens
def t_DO(t):
    r'do(?=[\:])'
    return t

def t_WHILE(t):
    r'while(?=[\(| ])'
    return t

def t_INTDec(t):
    r'int(?=[ ])'
    return t

def t_IF(t):
    r'if(?=[\(| ])'
    return t

def t_ELSE(t):
    r'else(?=\:)'
    return t
    
def t_ELIF(t):
    r'elif(?=[\(| ])'
    return t


def t_LCPARENT(t):
    r'\('
    t.lexer.paren_count += 1
    return t

def t_RCPARENT(t):
    r'\)'
    t.lexer.paren_count -= 1
    return t

def t_AND(t):
    r'and(?=[\( ])'
    return t

def t_OR(t):
    r'or(?=[\( ])'
    return t

def t_NUM(t):
    r'\d+'
    return t

def t_ID(t):
    r'\w+'
    return t

def t_EQUIV(t):
    r'\=\='
    return t

def t_ATRIB(t):
    r'\='
    return t

def t_error(t):
    print('Illegal character: ' + t.value[0])
    t.lexer.skip(1)
    return

def t_comment(t):
    r'\#.*'
    pass


t_ignore = '\r'


 
#  --- INDENTATION ---

NO_INDENT = 0
MAY_INDENT = 1
MUST_INDENT = 2


def track_tokens_filter(lexer, tokens):
    lexer.at_line_start = at_line_start = True
    indent = NO_INDENT
    saw_colon = False
    for token in tokens:
        token.at_line_start = at_line_start

        if token.type == "COLON":
            at_line_start = False
            indent = MAY_INDENT
            token.must_indent = False
        elif token.type == "NEWLINE":
            at_line_start = True
            if indent == MAY_INDENT:
                indent = MUST_INDENT
            token.must_indent = False
        elif token.type == "WS":
            assert token.at_line_start == True
            at_line_start = True
            token.must_indent = False
            #print(token)
        else:
            # A real token; only indent after COLON NEWLINE
            if indent == MUST_INDENT:
                token.must_indent = True
            else:
                token.must_indent = False
            at_line_start = False
            indent = NO_INDENT
            #print(token.at_line_start, token.must_indent)

        yield token
        lexer.at_line_start = at_line_start


def _new_token(type, lineno):
    tok = lex.LexToken()
    tok.type = type
    tok.value = None
    tok.lineno = lineno
    return tok

# Synthesize a DEDENT tag
def DEDENT(lineno):
    return _new_token("DEDENT", lineno)

# Synthesize an INDENT tag
def INDENT(lineno):
    return _new_token("INDENT", lineno)




# Track the indentation level and emit the right INDENT / DEDENT events.
def indentation_filter(tokens):
    # A stack of indentation levels; will never pop item 0
    levels = [0]
    token = None
    depth = 0
    prev_was_ws = False
    for token in tokens:
        # WS only occurs at the start of the line
        # There may be WS followed by NEWLINE so
        # only track the depth here.  Don't indent/dedent
        # until there's something real.
        if token.type == "WS":
            assert depth == 0
            depth = len(token.value)
            prev_was_ws = True
            # WS tokens are never passed to the parser
            continue

        if token.type == "NEWLINE":
            depth = 0
            if prev_was_ws or token.at_line_start:
                # ignore blank lines
                continue
            # pass the other cases on through
            yield token
            continue

        # then it must be a real token (not WS, not NEWLINE)
        # which can affect the indentation level

        prev_was_ws = False
        if token.must_indent:
            # The current depth must be larger than the previous level
            if not (depth > levels[-1]):
                raise IndentationError("expected an indented block")

            levels.append(depth)
            yield INDENT(token.lineno)
        elif token.at_line_start:
            # Must be on the same level or one of the previous levels
            if depth == levels[-1]:
                # At the same level
                pass
            elif depth > levels[-1]:
                #print(token, token.at_line_start, depth, levels)
                raise IndentationError(
                    "indentation increase but not in new block")
            else:
                # Back up; but only if it matches a previous level
                try:
                    i = levels.index(depth)
                except ValueError:
                    raise IndentationError("inconsistent indentation")
                for _ in range(i + 1, len(levels)):
                    yield DEDENT(token.lineno)
                    levels.pop()

        yield token

    ### Finished processing ###

    # Must dedent any remaining levels
    if len(levels) > 1:
        assert token is not None
        for _ in range(1, len(levels)):
            yield DEDENT(token.lineno)


# The top-level filter adds an ENDMARKER, if requested.
# Python's grammar uses it.
def filter(lexer, add_endmarker=True):
    token = None
    tokens = iter(lexer.token, None)
    tokens = track_tokens_filter(lexer, tokens)
    for token in indentation_filter(tokens):
        yield token

    if add_endmarker:
        lineno = 1
        if token is not None:
            lineno = token.lineno
        yield _new_token("ENDMARKER", lineno)

# Combine Ply and my filters into a new lexer


class IndentLexer(object):

    def __init__(self, debug=0, optimize=0, lextab='lextab', reflags=0):
        self.lexer = lex.lex(debug=debug, optimize=optimize,
                             lextab=lextab, reflags=reflags)
        self.token_stream = None

    def input(self, s, add_endmarker=True):
        self.lexer.paren_count = 0
        self.lexer.input(s)
        self.token_stream = filter(self.lexer, add_endmarker)

    def token(self):
        try:
            return next(self.token_stream)
        except StopIteration:
            return None

lexer = IndentLexer()
with open("tests/random_test.plc") as f:
    content = f.read()

lexer.input(content)
stream = lexer.token_stream
for token in stream:
    print(f"({token.type} {repr(token.value)} {token.lineno})")



#read from stdin 
'''
try:
    for linha in sys.stdin:
        lexer.input(linha) 
        simb = lexer.token()
        while simb:
            print(simb)
            simb = lexer.token()
except KeyboardInterrupt:
    print('\nKeyboard Interruption')
'''