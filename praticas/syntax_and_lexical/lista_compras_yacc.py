import sys
import ply.yacc as yacc

from lista_compras_lex import tokens


def p_lista(p):
    "lista : seccoes"
    print("Valor total das compras: ",p[1])


def p_seccoes_seccao(p):
    "seccoes : seccoes seccao"
    p[0] = p[1] + p[2]


def p_seccoes_empty(p):
    "seccoes : "
    p[0] = 0


def p_seccao(p):
    "seccao : ID ':' produtos"
    p[0] = p[3] 

def p_produtos_produto(p):
    "produtos : produto"
    p[0] =p[1]
    
def p_produtos_produtos(p):
    "produtos : produtos produto"
    p[0] = p[1] + p[2]
  
def p_produto(p):
    "produto : indent '-' cod SEP prod SEP FLOAT SEP INT ';'"
    p[0] = p[7] * p[9]

def p_indent(p):
    "indent : TAB"

def p_cod(p):
    "cod : INT"
def p_prod(p):
    "prod : ID"
    
def p_error(p):
    print('Syntax error!\np -> ', p)
    parser.sucesso = False
    
#inicio do Parser e do Processamento
parser = yacc.yacc()

parser.sucesso = True

f = open('lista_compras_exe.txt')
content = f.read()

parser.parse(content)
if (parser.sucesso):
   print("Lista de Compras bem escrita e Reconhecida")
