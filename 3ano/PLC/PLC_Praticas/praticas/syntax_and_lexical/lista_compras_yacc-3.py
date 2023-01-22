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
    # adicionar seccao ao conjunto de seccoes
    if p[1] in p.parser.seccoes:
        print('Aviso! Secções repetidas: ' + p[1])
    else:
        p.parser.seccoes.add(p[1])


def p_produtos_produto(p):
    "produtos : produto"
    p[0] =p[1]
    
def p_produtos_produtos(p):
    "produtos : produtos produto"
    p[0] =p[1] + p[2]
  


def p_produto(p):
    "produto : '-' INT SEP ID SEP FLOAT SEP INT ';'"
    p[0] = p[6] * p[8]
    info_produto = {
        'name': p[4],
        'price': p[6],
    }
    if p[2] in p.parser.produtos:
        if info_produto == p.parser.produtos[p[2]]:
            print('Aviso! Múltiplas entradas do mesmo produto:', p[2])
        else:
            print('Erro! Produtos diferentes com o mesmo ID:', p[2])
    else:
        p.parser.produtos[p[2]] = info_produto

def p_error(p):
    print('Syntax error!')
    parser.sucesso = False

#inicio do Parser e do Processamento
parser = yacc.yacc()

parser.sucesso = True
parser.seccoes = set()
parser.produtos = dict()

f = open('lista_compras_exe.txt')
content = f.read()

parser.parse(content)
if (parser.sucesso):
    print("Parser.seccoes -> ", parser.seccoes)
    print("Parser.produtos -> ", parser.produtos)
    print("Lista de Compras Correta: Reconhecida e Processada")

