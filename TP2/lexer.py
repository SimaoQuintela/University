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
    'INPUT'  
)

literals = [',', ':']


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
    return t

def t_RCPARENT(t):
    r'\)'
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

with open("tests/random_test.txt") as f:
    content = f.read()

lexer.input(content)
for token in lexer:
    print(token)


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