# ------------------------------------------------------------
# somador-ply.py
#
# somador de números
# tokens: on, off, = e \d+
# ------------------------------------------------------------
import ply.lex as lex
import sys

# My state
semaforo = False
soma = 0
 
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
    global soma
    print("Soma atual = ", soma)
    soma = 0
    return t

def t_ON(t):
    r'[oO][nN]'
    global semaforo
    semaforo = True
    return t

def t_OFF(t):
    r'[oO][fF][fF]'
    global semaforo
    semaforo = False
    return t
 
# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    global soma
    if (semaforo):
        soma = soma + int(t.value)   
    t.value = int(t.value)
    return t
 
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
# Error handling rule
def t_error(t):
    # print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
 
# Build the lexer
lexer = lex.lex()
 
# Reading input
for linha in sys.stdin:
    lexer.input(linha) 
    for tok in lexer:
        pass
        
