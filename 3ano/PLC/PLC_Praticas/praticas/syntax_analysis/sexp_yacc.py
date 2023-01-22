import ply.yacc as yacc
import sys

from sexp_lex import tokens

## incio da GIC

def p_lisp(p):
    "lisp : sexp"
    print('Parsing completed succesfully! ')


def p_sexp_pal(p):
    "sexp : PAL"
    print('Reconheci o atomo ', p[1])


def p_sexp_num(p):
    "sexp : NUM"
    print('Reconheci um numero ', p[1])

def p_sexp_sexplist(p):
    "sexp : LPAREN sexplist RPAREN"
    print('Reconheci uma lista completa')

def p_sexplist_sexp(p):
    "sexplist : sexp sexplist"
    print('Reconheci uma cabeça e cauda ')


def p_sexplist_empty(p):
    "sexplist : "
    print('Reconheci uma lista vazia ')


def p_error(p):
    parser.success = False
    print('Syntax error!')

###inicio do parsing
parser = yacc.yacc()
parser.success = True

fonte = ""
for line in sys.stdin:
    fonte += line
     
parser.parse(fonte)

