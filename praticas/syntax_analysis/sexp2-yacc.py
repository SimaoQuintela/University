import ply.yacc as yacc
import sys

from sexp_lex import tokens

## incio da GIC

def p_lisp(p):
    "lisp : sexp"
    print('Parsing completed succesfully! Value synthesized: ', p[1])


def p_sexp_pal(p):
    "sexp : PAL"
    p[0] = p[1]

def p_sexp_num(p):
    "sexp : NUM"
    p[0] = str(p[1])

def p_sexp_sexplist(p):
    "sexp : LPAREN sexplist RPAREN"
    p[0] = p[2]


def p_sexplist_sexp(p):
    "sexplist : sexp sexplist"
    p[0] = p[1]+ " , " +p[2]


def p_sexplist_empty(p):
    "sexplist : "
    p[0] = "$"


def p_error(p):
    parser.success = False
    print('Syntax error!')
    exit()

###inicio do parsing
parser = yacc.yacc()
parser.success = True

for linha in sys.stdin:
    parser.parse(linha)
