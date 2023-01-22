# Aula 11: 2021-05-11, jcr
#
# Analex para o recursivo descendente de árvores binárias
#
import ply.lex as lex

tokens = ['NUM', 'AP', 'FP']

t_NUM = r'\d+'
t_AP = r'\('
t_FP = r'\)'

t_ignore = " \t\n"

def t_error(t):
    # print("Caráter ilegal: ", t.value[0])
    t.lexer.skip(1)
    return t

# build the lexer
lexer = lex.lex()
