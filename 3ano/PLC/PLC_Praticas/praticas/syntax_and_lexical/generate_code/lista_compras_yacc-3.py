# Gramática Tradutora para interpretar uma Linguagem 
##  de Atribuições gerando a sua representação em Assembly
import sys

#--Definição e Geração do Analisador Léxico
import ply.lex as lex

literals = ['(', ')', '+', '-', '*', '/', '=']
tokens   = ["NUM", "ID", "PRINT", "DUMP"]


def t_DUMP(t):
	r'dump'
	return t

def t_PRINT(t):
	r'print'
	return t

def t_ID(t):
	r'[a-z]+'
	return t

def t_NUM(t):
	r'\d+'
	t.value = int(t.value)
	return t

t_ignore = " \n\t"

def t_error(t):
	print("Illegal character:", t.value[0])
	t.lexer.skip(1)

lexer = lex.lex()
#--Definição e Geração do Analisador Sintático
import ply.yacc as yacc

def p_prog(p):
	"prog : statements"

def p_statements_list(p):
	"statements : statements statement"

def p_statements_one(p):
	"statements : statement"

def p_statement_atrib(p):
	"statement : atrib"

def p_statement_print(p):
	"statement : print"

def p_statement_dump(p):
	"statement : dump"

def p_atrib(p):
	"atrib : ID '=' aexp"
	var = p[1]
	p.parser.table[var] = p[3]

def p_print(p):
	"print : PRINT '(' aexp ')'"
	print("alguma coisa")
	print(p[3])

def p_dump(p):
	"dump : DUMP"
	print(p.parser.table)

def p_aexp_add(p):
	"aexp : aexp '+' term"
	print("somei")
	p[0] = p[1] + p[3] + "ADD\n"


def p_aexp_sub(p):
	"aexp : aexp '-' term"
	p[0] = p[1] + p[3] + "SUB\n"

def p_aexp_term(p):
	"aexp : term"
	p[0] = p[1]

def p_term_mul(p):
	"term : term '*' factor"
	p[0] = p[1] + p[3] + "MUL\n"

def p_term_div(p):
	"term : term '/' factor"
	p[0] = p[1] + p[3] + "DIV\n"

def p_term_factor(p):
	"term : factor"
	p[0] = p[1]

def p_factor_NUM(p):
	"factor : NUM"
	p[0] = f'PUSHI {p[1]}\n'

def p_factor_ID(p):
	"factor : ID"
	p[0] = p.parser.table[p[1]]

def p_factor_aexp(p):
	"factor : '(' aexp ')'"
	p[0] = p[2]


def p_error(p):
	print("Syntax error:", p)

###-- geração do parser e parsing do texto-fonte
parser = yacc.yacc()
parser.table = {}

fonte = ""
for linha in sys.stdin:
	fonte += linha
	
parser.parse(fonte)






