import ply.lex as lex
import sys


class LexerPLC(object):
    tokens = [
        'INTDec',
        'NUM',
        'ID',
        'ATRIB',
        'EQUIV',
        'LEQ',  # <= - (less or equal)
        'GEQ',  # >= - (greater or equal)
        'GT',   # >  - (greater than)
        'LT',   # <  - (less than)
        'NEQ',  # /= - (not equal -> NEQ -> NECC)
        'LCPARENT',
        'RCPARENT',
        'LSQBRACKET', # left square bracket
        'RSQBRACKET', # right square bracket
        'LCURLBRACKET',
        'RCURLBRACKET',
        'SUM',
        'SUB',
        'DIV',
        'MULT',
        'MOD',
        'INC',
        'DEC',
        'QUOTE', # Símbolo "
        'STRING',
        'NEWLINE',
        'COLON',
        'WS',
        'INDENT',
        'DEDENT',
        'ENDMARKER'
    ]

    RESERVED = {
        "if": "IF",
        "else": "ELSE",
        "assert": "ASSERT",
        "while" : "WHILE",
        "do": "DO",
        "print": "PRINT",
        "input": "INPUT",
        "and": "AND",
        "or": "OR",
        "not": "NOT",
        "def": "DEF",
        "call": "CALL",
    }

    tokens += list(RESERVED.values())

    literals = [',']

    t_INPUT = r'input'
    t_PRINT = r'print'
    t_LCURLBRACKET = r'\{'
    t_RCURLBRACKET = r'\}'
    t_NOT = r'not'
    t_NEQ = r'\/\='
    t_COLON = r':'
    t_QUOTE = r'\"'
    t_MOD = r'\%'
    t_INC = r'\+\+'
    t_DEC = r'\-\-'
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_DIV = r'\/'
    t_MULT = r'\*'
    t_LSQBRACKET = r'\['
    t_RSQBRACKET = r'\]'
    t_LEQ = r'\<\='
    t_GEQ = r'\>\='
    t_GT = r'\>'
    t_LT = r'\<'
    t_EQUIV = r'\=\='
    t_ATRIB = r'\='

    # returns the content inside quotes
    def t_STRING(self, t):
        r'(?<=\")[A-Za-z0-9\, !-()\?\-\:\\]*(?=\")'
        return t

    def t_NUM(self, t):
        r'\d+'
        return t

    # (?= ) - lookahead, looks for a white space after de int keyword
    #  cover the cases:
    #    - int x       
    #    - intare x
    # without the lookahead both would be considered INT tokens
    def t_INTDec(self, t):
        r'int(?=[ ])'
        return t

    def t_DEF(self, t):
        r'def(?=[ ])'
        return t

    def t_CALL(self, t):
        r'\w+\(\)'
        return t

    def t_DO(self, t):
        r'do(?=[\:])'
        return t

    def t_WHILE(self, t):
        r'while(?=[\(| ])'
        return t

    def t_ASSERT(self, t):
        r'assert(?=[\(| ])'
        return t

    def t_IF(self, t):
        r'if(?=[\(| ])'
        return t

    def t_ELSE(self, t):
        r'else(?=\:)'
        return t

    def t_LCPARENT(self, t):
        r'\('
        t.lexer.paren_count += 1
        return t

    def t_RCPARENT(self, t):
        r'\)'
        t.lexer.paren_count -= 1
        return t

    def t_AND(self, t):
        r'and(?=[\( ])'
        return t

    def t_OR(self, t):
        r'or(?=[\( ])'
        return t

    def t_ID(self, t):
        r'\w+'
        t.type = self.RESERVED.get(t.value, "ID")
        return t

    def t_comment(self, t):
        r'\#.*'
        pass

    def t_WS(self, t):
        r'[ ]+'
        t.type = "WS"
        if t.lexer.at_line_start and t.lexer.paren_count == 0:
            return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        t.type = "NEWLINE"
        if t.lexer.paren_count == 0:
            return t

    def t_error(self, t):
        print("Illegal character:", t.value[0])
        t.lexer.skip(1)
        return

    t_ignore = '\r'

    #----- INDENTATION ----------------------------
    NO_INDENT = 0
    MAY_INDENT = 1
    MUST_INDENT = 2

    """
    A seguinte função identifica os tokens 'COLON', 'NEWLINE' e 'WS' e utiliza-os para:
    - identificar quais os tokens que devem ser indentados
    - identificar quais os tokens no início das linhas para verificar o nível da indentação
    """
    def _track_tokens_filter(self, tokens):
        self.lexer.at_line_start = at_line_start = True
        indent = self.NO_INDENT
        saw_colon = False

        result = []
        for token in tokens:
            token.at_line_start = at_line_start

            if token.type == "COLON":
                at_line_start = False
                indent = self.MAY_INDENT
                token.must_indent = False
            elif token.type == "NEWLINE":
                at_line_start = True
                if indent == self.MAY_INDENT:
                    indent = self.MUST_INDENT
                token.must_indent = False
            elif token.type == "WS":
                at_line_start = True
                token.must_indent = False
            else:
                token.must_indent = int(indent == self.MUST_INDENT)
                at_line_start = False
                indent = self.NO_INDENT

            self.lexer.at_line_start = at_line_start
            result.append(token)
        return result

    def _new_token(self, type, lineno):
        tok = lex.LexToken()
        tok.type = type
        tok.value = None
        tok.lineno = lineno
        return tok

    """
    Nesta função vamos começar a calcular as profundidades das indentações e a emitir os tokens INDENT e DEDENT para criar os blocos
    Nos 'WS' vamos calcular quantos espaços foram dados como indentação e retemos o token neste filtro
    Nos 'NEWLINE' resetamos a depth
    Nos restantes verificamos se a indentação está a acontecer e se a respectiva depth está a ser respeitada e emitimos os seus tokens INDENT e DEDENT
    No final criamos DEDENTS que estejam em falta devido à terminação do ficheiro num estado aninhado
    """
    def _indentation_filter(self, tokens):
        levels = [0]
        token = None
        depth = 0
        prev_was_ws = False
        result = []

        DEDENT = lambda lineno : self._new_token("DEDENT", lineno)
        INDENT = lambda lineno : self._new_token("INDENT", lineno)

        for token in tokens:
            if token.type == "WS":
                depth = len(token.value)
                prev_was_ws = True
                continue

            if token.type == "NEWLINE":
                depth = 0
                # ignore blank lines
                if prev_was_ws or token.at_line_start:
                    continue
                result.append(token)
                continue

            if token.must_indent:
                # The current depth must be larger than the previous level
                if not (depth > levels[-1]):
                    raise IndentationError("expected an indented block")
                levels.append(depth)
                result.append(INDENT(token.lineno))
            elif token.at_line_start:
                # Must be on the same level or one of the previous levels
                if depth > levels[-1]:
                    raise IndentationError("indentation increase but not in new block")
                elif depth < levels[-1]:
                    # Back up; but only if it matches a previous level
                    try:
                        i = levels.index(depth)
                    except ValueError:
                        raise IndentationError("inconsistent indentation")
                    for _ in range(i + 1, len(levels)):
                        levels.pop()
                        result.append(DEDENT(token.lineno))
            prev_was_ws = False
            result.append(token)

        ### Finished processing ###
        if len(levels) > 1:
            assert token is not None
            result += [DEDENT(token.lineno) for _ in range(1, len(levels))]

        return result

    # Criar a Nova Stream 
    def _filter(self):
        token = None
        tokens = iter(self.lexer.token, None)
        tokens = self._track_tokens_filter(tokens)

        for token in self._indentation_filter(tokens):
            yield token

        lineno = 1 if token is None else token.lineno
        yield self._new_token("ENDMARKER", lineno)


    def __init__(self, debug=0, optimize=0, lextab='lextab', reflags=0):
        self.lexer = lex.lex(module=self, debug=debug, optimize=optimize, lextab=lextab, reflags=reflags)
        self.token_stream = None

    def input(self, s):
        self.lexer.paren_count = 0
        self.lexer.input(s)
        self.token_stream = self._filter()

    def token(self):
        try:
            return next(self.token_stream)
        except StopIteration:
            return None



with open(f"tests/{sys.argv[1]}.plc") as f:
    content = f.read()

lexer = LexerPLC()
lexer.input(content)

for token in lexer.token_stream:
    print(f"({token.type} {repr(token.value)} {token.lineno})")