import ply.lex as lex
import sys

## Analisador Léxico para alguns dos símbolos terminias usados 
### num Ling.Programação tipo Python
###  x = y * 2; (6 Tokens, 2 Identificadores , 0 Palavras Reservadas, 1 Inteiro, 3 Sinais)
###  a = X + Yvar
###  if ( xyz == 12 ): print( xyz/4 , a )
###  lst = [ 1, 2, 3 ,4]

tokens = (
    'LPAREN',
    'RPAREN',
    'VIRG',
    'IGUAL',
    'EQ',
    'MAIS',
    'MENOS',
    'DIV',
    'VEZES',
    'LISTAD',
    'LISTAE',
    'DOISpt',
    'IF',
    'ELSE', 
    'ID',
    'Nint',
    'Nreal'
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LISTAD = r'\['
t_LISTAE = r'\]'
t_VIRG   = r'\,'
t_DOISpt = r'\:'
t_EQ     = r'\=\='
t_IGUAL  = r'\='
t_MAIS   = r'\+'
t_DIV    = r'\/'
t_MENOS  = r'\-'
t_VEZES  = r'\*'

def t_Nreal(t):
    r'[0-9]+\.[0-9]+'
    return t
def t_Nint(t):
    r'[0-9]+'
    return t
    
def t_IF(t):
    r'(?i)if'
    return t

def t_ELSE(t):
    r'(?i:else)'
    return t
     
def t_ID(t):
    r'[a-zA-Z]+'
    return t
    
t_ignore = ' \r\n\t'

def t_error(t):
    print('Illegal character: ' + t.value[0])
    t.lexer.skip(1)
    return


lexer = lex.lex() # cria um AnaLex especifico a partir da especificação acima usando o gerador 'lex' do objeto 'lex'

# Reading input
for linha in sys.stdin:
    lexer.input(linha) 
    simb = lexer.token()
    while simb:
        print(simb)
        simb = lexer.token()


