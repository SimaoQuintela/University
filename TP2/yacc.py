from lexer import tokens, lexer, IndentLexer
import ast
import ply.yacc as yacc

# ---------------- Programa ----------------
def p_Programa_Init(p):
    "ProgramaInit : Programa ENDMARKER"
    parser.assembly = f"{p[1]}"

def p_Programa(p):
    "Programa : Corpo"
    p[0] = f'START\n{p[1]}STOP'

def p_Programa_Decls(p):
    "Programa : Decls Corpo"
    p[0] = f'{p[1]}START\n{p[2]}STOP'

# ---------------- Corpo ----------------
def p_Corpo(p):
    "Corpo : Proc Newline"
    p[0] = f'{p[1]}{p[2]}'

def p_Corpo_Proc(p):
    "Corpo : Corpo Proc Newline"
    p[0] = f'{p[1]}{p[2]}{p[3]}'

def p_Corpo_Newline(p):
    "Corpo : Newline"
    p[0] = f'{p[1]}'

# ---------------- Newline ----------------
def p_Newline_Empty(p):
    "Newline : "
    p[0] = ''

def p_Newline(p):
    "Newline : NEWLINE"
    p[0] = ''


# ---------------- Declarations ----------------
def p_Decls(p):
    "Decls : Decl Newline"
    p[0] = f'{p[1]}{p[2]}'

def p_Decls_Recursiva(p):
    "Decls : Decls Decl Newline"
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

# ---------------- Procedures ----------------
def p_Proc_Atrib(p):
    "Proc : Atrib"
    p[0] = p[1]

def p_Proc_Print(p):
    "Proc : Print"
    p[0] = f'{p[1]}'

def p_Proc_If(p):
    "Proc : If"
    p[0] = f'{p[1]}'


# ---------------- If Else - Flux Control ----------------
def p_If(p):
    "If : IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent"
    p[0] = f'{p[3]}JZ label{p.parser.labels}\n{p[8]}label{p.parser.labels}: NOP\n'
    p.parser.labels += 1

def p_If_Else(p):
    "If : IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent ELSE COLON Newline INDENT Corpo DEDENT"
    p[0] = f'{p[3]}JZ l{p.parser.labels}\n{p[8]}JUMP l{p.parser.labels}f\nl{p.parser.labels}: NOP\n{p[14]}l{p.parser.labels}f: NOP\n'

# ---------------- Indentation ----------------
def p_Dedent_Rec(p):
    "Dedent : Dedent DEDENT"
    p[0] = f'{p[0]}{p[1]}'

def p_Dedent_Empty(p):
    "Dedent : "
    p[0] = ''

# ---------------- Conditions ----------------
def p_Cond_GT(p):
    "Cond : Expr GT Expr"
    p[0] = f'{p[1]}{p[3]}SUP\n'

def p_Cond_LT(p):
    "Cond : Expr LT Expr"
    p[0] = f'{p[1]}{p[3]}INF\n'

def p_Cond_GEQ(p):
    "Cond : Expr GEQ Expr"
    p[0] = f'{p[1]}{p[3]}SUPEQ\n'

def p_Cond_LEQ(p):
    "Cond : Expr LEQ Expr"
    p[0] = f'{p[1]}{p[3]}INFEQ\n'

def p_Cond_EQUIV(p):
    "Cond : Expr EQUIV Expr"
    p[0] = f'{p[1]}{p[3]}EQUAL\n'

def p_Cond_NEQ(p):
    "Cond : Expr NEQ Expr"
    p[0] = f'{p[1]}{p[3]}EQUAL\nNOT\n'

def p_Cond_OR(p):
    "Cond : Cond OR Cond"
    p[0] = f'{p[1]}{p[3]}ADD\nPUSHI 1\nSUPEQ\n'

def p_Cond_AND(p):
    "Cond : Expr AND Expr"
    p[0] = f'{p[1]}{p[3]}ADD\nPUSHI 2\nSUPEQ\n'

def p_Cond_NOT(p):
    "Cond : NOT Cond"
    p[0] = f'{p[2]}NOT\n'

# ---------------- Atribuitions ----------------
def p_Atrib_Expr(p):
    "Atrib : ID ATRIB Expr"
    if p[1] in p.parser.registers:
        p[0] = f'{p[3]}STOREG {p.parser.registers.get(p[1])}\n'
    else:
        print(f"Erro: Variável {p[1]} não definida.")
        parser.success = False

def p_Atrib_Input(p):
    "Atrib : ID ATRIB Input"
    if p[1] in p.parser.registers:
        p[0] = f'{p[3]}READ\nATOI\nSTOREG {p.parser.registers.get(p[1])}\n'
    else:
        print(f"Erro, variável {p[1]} não inicializada")
        parser.success = False

# ---------------- Print ----------------
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
    p[0] = f'{p[1]}WRITEI\nPUSHS "\\n"\nWRITES\n'

def p_Argument_Expr(p):
    "Argument : Expr"
    p[0] = f'{p[1]}WRITEI\nPUSHS "\\n"\nWRITES\n'

# ---------------- Expressions ----------------
def p_Expr_Var(p):
    "Expr : Var"
    p[0] = p[1]

def p_Expr_Num(p):
    "Expr : NUM"
    p[0] = f'PUSHI {p[1]}\n'

def p_Expr_Soma(p):
    "Expr : Expr SUM Expr"
    p[0] = f'{p[1]}{p[3]}ADD\n'

def p_Expr_Sub(p):
    "Expr : Expr  SUB Expr"
    p[0] = f'{p[1]}{p[3]}SUB\n'

def p_Expr_Mult(p):
    "Expr : Expr  MULT Expr"
    p[0] = f'{p[1]}{p[3]}MUL\n'

def p_Expr_Div(p):
    "Expr : Expr  DIV Expr"
    p[0] = f'{p[1]}{p[3]}DIV\n'

def p_Expr_Mod(p):
    "Expr : Expr MOD Expr"
    p[0] = f'{p[1]}{p[3]}MOD\n'

def p_Expr_Inc(p):
    "Expr : ID INC"
    p[0] = f'PUSHG {p.parser.registers.get(p[1])}\nPUSHI 1\nADD\n'

def p_Expr_Dec(p):
    "Expr : ID DEC"
    p[0] = f'PUSHG {p.parser.registers.get(p[1])}\nPUSHI 1\nSUB\n'

def p_Var(p):
    "Var : ID"
    if p[1] in p.parser.registers:
        if p[1] in p.parser.ints:
            p[0] = f'PUSHG {p.parser.registers.get(p[1])}\n'
        else:
            parser.success = False
            print("Erro: A Variável não é do tipo int.")
    else:
        parser.success = False
        print("Erro: Variável não definida")

# ---------------- Input ----------------
def p_Input(p):
    "Input : INPUT LCPARENT String RCPARENT"
    p[0] = f'{p[3]}'

# ---------------- Strings ----------------
def p_String(p):
    "String : QUOTE STRING QUOTE"
    p[0] = f'PUSHS "{p[2]}"\nWRITES\n'

def p_String_Empty(p): 
    "String :  "
    p[0] = ''


# ---------------- Errors ----------------
def p_error(p):
    print('Syntax error!\np -> ', p)
    parser.sucesso = False


precedence = (
    ("left", "SUM", "SUB"),
    ("left", "MULT", "DIV")
)

class PLCParser(object):

    def __init__(self, lexer=None):
        if lexer is None:
            lexer = IndentLexer()
        self.lexer = lexer
        self.parser = yacc.yacc(start="ProgramaInit")

    def parse(self, code):
        self.lexer.input(code)
        result = self.parser.parse(lexer=self.lexer)
        return ast.Module(result)

lexer = IndentLexer()
parser = yacc.yacc()

parser.success = True
parser.registers = {}
parser.assembly = ""
parser.gp = 0
parser.ints = []
parser.labels = 0

with open("tests/random_test.plc") as f:
    content = f.read()

lexer.input(content)
parser.parse(lexer=lexer)

if parser.success:
    print("Ficheiro lido com sucesso")

    f_out = open('tests/random_test.vm', 'w')
    f_out.write(parser.assembly)
    f_out.close()
    print("Código assembly gerado e guardado.")
else:
    print("Erro ao compilar")

