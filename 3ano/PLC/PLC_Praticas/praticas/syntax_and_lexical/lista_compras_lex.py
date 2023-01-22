import ply.lex as lex

tokens = ['ID', 'INT', 'FLOAT', 'SEP', 'INDENT']

literals = ['-', ',', ':', ';']


t_SEP = r'::'
t_ID = r'\w+'
t_INDENT = r' \t'


def t_FLOAT(t):
    r'\d+.\d+'
    t.value = float(t.value)
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \n'

def t_error(t):
    print('Illegal character: ' + t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


with open('lista_compras_exe.txt') as f:
    content = f.read()

lexer.input(content)

#for token in lexer:
    #print(token)

