# 0052 - R
# 0072 - r
import ply.lex as lex
import sys

# Already implemented:
# - = and ==         - declarations and equality
# - if, elif, else   - flux control
# - and, or          - basic logic operators

tokens = (
    'INTDec',
    'NUM',
    'ID',
    'ATRIB',
    'EQUIV',
    'IF',
    'ELSE',
    'ELIF',
    'LCPARENT',
    'RCPARENT',
    'AND',
    'OR',
    'INC',
    'DEC',
# ------------ #
    'DO',
    'WHILE'

)

literals = [',', ':']

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
    return t

def t_RCPARENT(t):
    r'\)'
    return t

def t_AND(t):
    r'and(?=[\(\) ])'
    return t

def t_OR(t):
    r'or(?=[\(\) ])'
    return t

def t_NUM(t):
    r'\d+'
    return t

def t_ID(t):
    r'\w+'
    return t

def t_INC(t):
    r'\+\+'
    return t

def t_DEC(t):
    r'\-\-'
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

t_ignore = ' \r\t\n'


lexer = lex.lex()

with open("examples/tests.txt") as f:
    content = f.read()

lexer.input(content)
for token in lexer:
    print(token)


"""
read on stdin 
for linha in sys.stdin:
    lexer.input(linha) 
    simb = lexer.token()
    while simb:
        print(simb)
        simb = lexer.token()
"""