# abin_lex.py
#
# ()
# (15 () ())
# (40 (20 () ()) (50 () ()))
#
# T = {num, '(', ')'}
#
# ABin -> '(' num ABin Abin ')'
#       | '(' ')'
#
import ply.lex as lex

tokens = ['num']
literals = ['(', ')']

t_num = r'[+\-]?\d+'

t_ignore = " \t\n"

def t_error(t):
    print("Caráter ilegal: ", t.value[0])
    t.lexer.skip(1)

# build the lexer
lexer = lex.lex()
