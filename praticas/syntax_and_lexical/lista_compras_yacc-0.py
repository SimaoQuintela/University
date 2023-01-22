import sys
import ply.yacc as yacc

from lista_compras_lex import tokens

def p_lisp_grammar(p):
    """
    lista : seccoes
    seccoes : seccoes seccao
    seccoes : 
    seccao : ID ':' produtos
    produtos : produto
    produtos : produtos produto
    produto : INDENT '-' codP SEP nomeP SEP precU SEP qt ';'
    codP  :  INT
    nomeP :  ID
    precU :  FLOAT
    qt    :  INT 
    """


def p_error(p):
    print('Syntax error!\np -> ', p)
    parser.sucesso = False

#inicio do Parser e do Processamento
parser = yacc.yacc()

parser.sucesso = True
parser.seccoes = set()
parser.produtos = dict()

#with open('lista_compras_exe.txt') as f:

f = open('lista_compras_exe.txt')
content = f.read()

#content=""
#for linha in sys.stdin:
#    content += linha

parser.parse(content)
if (parser.sucesso):
    print("Parser.seccoes -> ", parser.seccoes)
    print("Parser.produtos -> ", parser.produtos)
    print("Lista de Compras bem escrita e Reconhecida")
   
