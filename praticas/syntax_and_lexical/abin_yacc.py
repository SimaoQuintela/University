# abin_yacc.py
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
import ply.yacc as yacc
import sys

# Get the token map from the lexer.  This is required.
from abin_lex import tokens

# Production rules
def p_ABin(p):
    "ABin : '(' num ABin ABin ')'"
    p[0] = "{\n\t\"root\": " + p[2] + ",\n\t\"left\": " + p[3] + ",\n\t\"right\": " + p[4] + "\n}"

def p_ABin_empty(p):
    "ABin : '(' ')'"
    p[0] = "null"

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input: ", p)
 
 # Build the parser
parser = yacc.yacc()

# reading input
for linha in sys.stdin:
    result = parser.parse(linha)
    print(result)