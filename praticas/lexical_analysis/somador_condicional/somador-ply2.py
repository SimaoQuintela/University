# ------------------------------------------------------------
# somador-ply.py
#
# somador de números
# tokens: on, off, = e \d+
# ------------------------------------------------------------
import ply.lex as lex
import sys
 
# List of token names.   This is always required
tokens = (
    'ON',
    'OFF',
    'DISPLAY',
    'NUMBER'
)

# Regular expression rules for simple tokens
def t_DISPLAY(t):
    r'='
    print("Soma = ", t.lexer.soma)
    return t
    
def t_ON(t):
    r'[oO][nN]|\+'
    t.lexer.semaforo = True
    return t
    
def t_OFF(t):
    r'[oO][fF][fF]|\-'
    t.lexer.semaforo = False
    return t
 
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    if (t.lexer.semaforo):
        t.lexer.soma +=  int(t.value)   
    return t
 
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

 
# Build the lexer
#lexer = lex.lex(optimize=1, lextab="lextab")
lexer = lex.lex()

# My state
lexer.semaforo = False
lexer.soma = 0
 
for linha in sys.stdin:
    lexer.input(linha) 
    tok = lexer.token()
    while tok:
        tok = lexer.token()

print("A soma calculada final e: ", lexer.soma)
   








