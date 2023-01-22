import ply.lex as lex
import sys

#Programa que gera um analizador lexico, nao e um analisador lexico em si
# [112]
# [ 1,2,3,4,5; 6]
# [Leander,10;Alda , 112; Joker ;7 ]

tokens = [
    'PRA',
    'PRF',
    'SOS',
    'V',
    'REAL',
    'INT',
    'PAL',
    'TRUE',
    'FALSE'
]

#declaração dos SINAIS que não tem ações semânticas associadas nem preferencias
t_PRA = r'\['
t_PRF = r'\]'
t_V = r'[;,]'

#declaração das Palavras-Reservadas e dos Simbolos de Classe (variáveis)
def t_TRUE(t):
    r'True'
    return t
def t_FALSE(t):
    r'False'
    return t
def t_PAL(t):
    r'[a-zA-Z]+'
    return t
    
def t_SOS(t):
    r'112'
    return t

def t_REAL(t):
    r'([0-9]+\.[0-9]+)'
    return t
    
soma = 0
def t_INT(t):
    r'[0-9]+'
    global soma
    soma += int(t.value)
    return t

#declaração dos Carateres que podem aparecer no texto de entrada e que devem ser ignorados
t_ignore = ' \n\t'
#declaração da ação a fazer relativa aos Carateres que NÃO podem aparecer no texto de entrada
def t_error(t):
    print('Carater ilegal: ',t.value)
    return

lexer = lex.lex()

for line in sys.stdin:
    lexer.input(line)
    tok = lexer.token()
    while tok:
        print(tok)
        #print(f'SOMA: {soma}') #imprime a soma após a leitura de cada tokrn
        tok = lexer.token()
    #print(f'SOMA: {soma}')    #imprime a soma no fim de cada linha
print(f'SOMA: {soma}')         #imprime a soma só no fim do texto


'''Sinais:
alt y => 2 identificadores
alty  => 1 identificador
alt + => alt é um identificador
alt+  => alt continua sendo un identificador
Quando aparecem o RL reconhece individualmente sem a existencia de espaços
Em caso de confusao usar como funcao
'''
