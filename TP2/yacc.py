from lexer import tokens
import ply.yacc as yacc

#def p_Programa(p):
#    "Programa : Corpo"
    #parser.assembly = f'START\n{p[1]}STOP'


def p_Programa_Decls(p):
    "Programa : Decls"
    #parser.assembly = f'{p[1]}START\n{p[2]}STOP'

def p_Decls(p):
    "Decls : Decl"
    p[0] = f'{p[1]}'

def p_Decls_Recursiva(p):
    "Decls : Decls Decl"
    p[0] = f'{p[1]}{p[2]}'


def p_Decl_Int(p):
    "Decl : INTDec nomeVar ATRIB NUM"
    p[0] = p[4]
    print(f"{p[2]} = {p[4]}")

def p_nome_var(p):
    "nomeVar : ID"
    p[0] = p[1]
    

def p_error(p):
    print('Syntax error!\np -> ', p)
    parser.sucesso = False


parser = yacc.yacc()

parser.success = True
parser.assembly = ""

f = open('examples/tests.txt', 'r')
inp = f.read()
parser.parse(inp)

if parser.success:
    print("Ficheiro lido com sucesso")