# Parser recursivo descendente, LL(1) para listas de inteiros
# 2021-05-11, jcr
#
#p1: Lista -> '[' Cont
#p2: Cont -> ']'
#p3:       | Elementos ']'
#p4: Elementos -> num ContElem
#p5: ContElem -> €
#p6:           | ',' Elementos

import sys
#from lista_lex import tokens
from lista_lex import lexer

def erro(esperado, recebido):
    print('Erro sintático: estava à espera de ', esperado, 'e recebi ', recebido)

def get_simb():
    tok = lexer.token()
    if tok:
        return tok.type

def rec_term(simb):
    global prox_simb
    if prox_simb == simb:
        prox_simb = get_simb()

def rec_Lista():
    global prox_simb
    if prox_simb == 'AP':
        rec_term('AP')
        rec_Cont()
    else:
        erro('AP', prox_simb)

def rec_Cont():
    global prox_simb
    if prox_simb == 'FP':
        rec_term('FP')
    elif prox_simb == 'NUM':
        rec_Elementos()
        rec_term('FP')
    else:
        erro('FP ou NUM', prox_simb)

def rec_Elementos():
    global prox_simb
    if prox_simb == 'NUM':
        rec_term('NUM') 
        rec_ContElem()
    else:   
        erro('NUM', prox_simb)

def rec_ContElem():
    global prox_simb
    if prox_simb == 'FP':
        pass
    elif prox_simb == 'VIRG':
        rec_term('VIRG')
        rec_Elementos()
    else:
        erro('FP ou VIRG', prox_simb)


# Main program
for linha in sys.stdin:
    lexer.input(linha)
    prox_simb = get_simb()
    #
    rec_Lista()
    #
    print('Frase analisada: ', linha)
