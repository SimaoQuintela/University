from lexer import tokens
import ply.yacc as yacc


def p_Programa(p):
    "Programa : Corpo"
    parser.assembly = f'START\n{p[1]}STOP'


def p_Programa_Decls(p):
    "Programa : Decls Corpo"
    parser.assembly = f'{p[1]}START\n{p[2]}STOP'

def p_Decls(p):
    "Decls : Decl"
    p[0] = f'{p[1]}'

def p_Decls_Recursiva(p):
    "Decls : Decls Decl"
    p[0] = f'{p[1]}{p[2]}'

def p_Decl_Int(p):
    "Decl : INTDec ID"
    if p[2] not in p.parser.registers:
        p.parser.registers.update({p[2] : p.parser.gp})
        p[0] = f'PUSHI 0\n'
        p.parser.ints.append(p[2])
        p.parser.gp += 1
    else:
        print("Erro: Variável já inicializada")
        parser.success = False

def p_Decl_Int_Val(p):
    "Decl : INTDec ID ATRIB NUM"
    if p[2] not in p.parser.registers:
        p.parser.registers.update({p[2] : p.parser.gp})
        p[0] = f'PUSHI {p[4]}\n'
        p.parser.ints.append(p[2])
        p.parser.gp += 1
    else:
        print("Erro: Variável já inicializada")
        parser.success = False

def p_Decl_Int_Input(p):
    "Decl : INTDec ID ATRIB Input"
    if p[2] not in p.parser.registers:
        p.parser.registers.update({p[2] : p.parser.gp})
        p.parser.ints.append(p[2])
        p[0] = f'{p[4]}READ\nATOI\nSTOREG {p.parser.registers.get(p[2])}\n'
        p.parser.gp += 1
    else:
        print("Erro variável já inicializada")
        parser.success = False

def p_Input(p):
    "Input : INPUT LCPARENT String RCPARENT"
    p[0] = f'{p[3]}'


def p_Corpo(p):
    "Corpo : Proc"
    p[0] = f'{p[1]}'

def p_Corpo_Proc(p):
    "Corpo : Corpo Proc"
    p[0] = f'{p[1]}{p[2]}'
"""

def p_Proc_Atrib(p):
    "Proc : Atrib"
    p[0] = p[1]
"""

def p_Atrib_Print(p):
    "Proc : Print"
    p[0] = f'{p[1]}'
    
def p_Print_NonFormatted(p):
    "Print : NonFormatted"
    p[0] = f'{p[1]}'

def p_NonFormatted(p):
    "NonFormatted : PRINT LCPARENT Argument RCPARENT"
    p[0] = f'{p[3]}'

def p_Argument_String(p):
    "Argument : String"
    p[0] = f'{p[1]}'

def p_Argument_Var(p):
    "Argument : Var"
    p[0] = f'{p[1]}PUSHS "\\n"\nWRITES\n'

def p_Var(p):
    "Var : ID"
    if p[1] in p.parser.registers:
        if p[1] in p.parser.ints:
            p[0] = f'PUSHG {p.parser.registers.get(p[1])}\nWRITEI\n'
        else:
            parser.success = False
            print("Erro: A Variável não é do tipo int.")
    else:
        parser.success = False
        print("Erro: Variável não definida")


def p_String(p):
    "String : QUOTE STRING QUOTE"
    p[0] = f'PUSHS "{p[2]}"\nWRITES\n'

def p_String_Empty(p): 
    "String :  "
    p[0] = ''

def p_error(p):
    print('Syntax error!\np -> ', p)
    parser.sucesso = False


parser = yacc.yacc()

parser.success = True
parser.registers = {}
parser.assembly = ""
parser.gp = 0
parser.ints = []
parser.labels = {}

f_inp = open('tests/random_test.txt', 'r')
inp = f_inp.read()
f_inp.close()
parser.parse(inp)

if parser.success:
    print("Ficheiro lido com sucesso")

    f_out = open('tests/random_test.vm', 'w')
    f_out.write(parser.assembly)
    f_out.close()
    print("Código assembly gerado e guardado.")
else:
    print("Erro ao compilar")