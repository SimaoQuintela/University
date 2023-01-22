# ------------------------------------------------------------
# somador-ply.py
#
# somador de números
# tokens: on+, on-, off, = e \d+
# ------------------------------------------------------------
import ply.lex as lex
import sys

# Declare the state
states = (
   ('soma','exclusive'),
   ('sub','exclusive'),
)
 
# List of token names.   This is always required
tokens = (
    'ON1',
    'ON2',
    'OFF',
    'DISPLAY',
    'NUMBER'
)
 
# Regular expression rules for tokens in initial state
def t_ANY_ON1(t):
    r'[Oo][Nn]\+'
    t.lexer.begin('soma')
def t_ANY_ON2(t):
    r'[Oo][Nn]\-'
    t.lexer.begin('sub') 
    
def t_ANY_DISPLAY(t):
    r'='
    print("soma = ", t.lexer.soma)
 
# Define a rule so we can track line numbers
def t_ANY_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ANY_ignore  = ' \t'
 
# Error handling rule: remaining chars
def t_ANY_error(t):
    t.lexer.skip(1)

# ---------------------------------------------------------------
# Regular expression rules for tokens in semaforo state
def t_soma_OFF(t):
    r'[oO][fF][fF]'
    t.lexer.begin('INITIAL')
def t_sub_OFF(t):
    r'[oO][fF][fF]'
    t.lexer.begin('INITIAL')

def t_soma_NUMBER(t):
    r'\d+'
    t.lexer.soma += int(t.value)  

def t_sub_NUMBER(t):
    r'\d+'
    t.lexer.soma -= int(t.value) 
    
# Build the lexer
lexer = lex.lex()

# My state
lexer.soma = 0
 
# Reading input
for linha in sys.stdin:
    lexer.input(linha) 
    tok = lexer.token()
    while tok:
        #print(tok)
        tok = lexer.token()

print("A soma calculada final e: ", lexer.soma)
      
