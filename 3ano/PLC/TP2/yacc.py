from lexer import lexer, LexerPLC
import ast
import ply.yacc as yacc
import sys

# ---------------- Programa ----------------
def p_Programa_Init(p):
    "ProgramaInit : Programa ENDMARKER"
    parser.assembly = f"{p[1]}"

def p_Programa(p):
    """Programa : Corpo
                | Decls Corpo"""
    decls = f'{p[1]}\n' if len(p) == 3 else ''
    p[0] = f'{decls}START\n{p[len(p) - 1]}STOP'

# ---------------- Corpo ----------------
def p_Corpo(p):
    """Corpo : Proc Newline
             | Corpo Proc Newline
             | Newline"""
    p[0] = "".join(p[1:])

# ---------------- Empty ----------------
def p_Empty(p):
    "Empty : "
    pass

# ---------------- Newline ----------------
def p_Newline(p):
    """Newline : NEWLINE
               | Empty"""
    p.parser.lineno += 1
    p[0] = ''

# ---------------- Indentation ----------------
def p_Dedent(p):
    """Dedent : Dedent DEDENT
              | Empty"""
    p[0] = ''

# ---------------- Declarations ----------------
def p_Decls(p):
    """Decls : Decl Newline
             | Decls Decl Newline"""
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

def p_Decl_Int_Array_Val(p):
    "Decl : INTDec ID LSQBRACKET NUM RSQBRACKET ATRIB ArrayValues"
    if p[2] not in p.parser.arrays:
        p.parser.registers.update({p[2]: (p.parser.gp-int(p[4]), int(p[4]))})
        p.parser.arrays.append(p[2])
        p[0] = f"{p[7]}"
    else:
        print("Array já inicializado")
        parser.success = False

def p_Decl_Int_Array(p):
    "Decl : INTDec ID LSQBRACKET NUM RSQBRACKET"
    if p[2] not in p.parser.arrays:
        # "x" : (gp, size)
        p.parser.registers.update({p[2]: (p.parser.gp, int(p[4]))})
        p.parser.arrays.append(p[2])
        p.parser.gp += int(p[4])
        p[0] = f"PUSHN {p[4]}\n"
    else:
        print("Array já inicializado")
        parser.success = False

def p_DEF(p):
    "Decl : Def"
    p[0] = f'{p[1]}'

# ---------------- Functions ----------------
def p_Def(p):
    """Def : DEF ID COLON Newline INDENT Corpo DEDENT
           | DEF ID COLON Newline INDENT Decls Corpo DEDENT"""
    name = f'function{len(p.parser.functions)}'
    body = "".join(p[6:len(p)-1])
    p[0] = f'JUMP {name}Ignore\n{name}:\n{body}RETURN\n{name}Ignore:\n\n'
    p.parser.functions[p[2]+"()"] = name

# ---------------- Arrays ----------------
def p_ArrayValues(p):
    "ArrayValues : LCURLBRACKET ArrayIntValues RCURLBRACKET"
    p[0]  = f'{p[2]}'

def p_ArrayIntValues_Rec(p):
    "ArrayIntValues : ArrayIntValues ',' Expr"
    p[0] = f'{p[1]}{p[3]}'
    p.parser.gp += 1

def p_ArrayIntValues(p):
    "ArrayIntValues : Expr"
    p[0] = f'{p[1]}'
    p.parser.gp += 1

# ---------------- Procedures ----------------
def p_Proc(p):
    """Proc : Atrib
            | Print
            | If
            | Cycle
            | Call
            | Assert"""
    p[0] = p[1]

# ---------------- Function calls ----------------
def p_Call(p):
    "Call : CALL"
    p[0] = f'PUSHA {p.parser.functions[p[1]]}\nCALL\n'

# ---------------- Asserts ----------------
def p_Assert(p):
    "Assert : ASSERT LCPARENT Cond RCPARENT"
    error_message = f'ERR "False assertion in line {p.parser.lineno}"'
    p[0] = f'{p[3]}JZ label{p.parser.labels}\nJUMP label{p.parser.labels}f\nlabel{p.parser.labels}: NOP\n{error_message}\nlabel{p.parser.labels}f: NOP\n'
    p.parser.labels += 1

# ---------------- If Else - Flux Control ----------------
def p_If(p):
    "If : IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent"
    p[0] = f'{p[3]}JZ label{p.parser.labels}\n{p[8]}label{p.parser.labels}: NOP\n'
    p.parser.labels += 1

def p_If_Else(p):
    "If : IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent ELSE COLON Newline INDENT Corpo DEDENT"
    p[0] = f'{p[3]}JZ label{p.parser.labels}\n{p[8]}JUMP label{p.parser.labels}f\nlabel{p.parser.labels}: NOP\n{p[14]}label{p.parser.labels}f: NOP\n'
    p.parser.labels += 1

# ---------------- Cycles - Flux Control ----------------
def p_Cycle(p):
    """Cycle : While
             | DoWhile"""
    p[0] = p[1]

def p_Do_While(p):
    "DoWhile : DO COLON Newline INDENT Corpo Dedent WHILE LCPARENT Cond RCPARENT NEWLINE"
    p[0] = f'label{p.parser.labels}:\n{p[5]}{p[9]}NOT\nJZ label{p.parser.labels}\n'
    p.parser.labels += 1

def p_While(p):
    "While : WHILE LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent"
    p[0] = f'label{p.parser.labels}c: NOP\n{p[3]}JZ label{p.parser.labels}f\n{p[8]}JUMP label{p.parser.labels}c\nlabel{p.parser.labels}f: NOP\n'
    p.parser.labels += 1

# ---------------- Conditions ----------------
condition_map ={
    ">": "SUP\n",
    "<": "INF\n",
    ">=": "SUPEQ\n",
    "<=": "INFEQ\n",
    "==": "EQUAL\n",
    "/=": "EQUAL\nNOT\n",
    "or": "ADD\nPUSHI 1\nSUPEQ\n",
    "and": "ADD\nPUSHI 2\nSUPEQ\n",
}

def p_Cond(p):
    """Cond : Expr GT Expr
            | Expr LT Expr
            | Expr GEQ Expr
            | Expr LEQ Expr
            | Expr EQUIV Expr
            | Expr NEQ Expr
            | Expr OR Expr
            | Expr AND Expr"""
    p[0] = f'{p[1]}{p[3]}{condition_map[p[2]]}'

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

def p_Atrib_INC_DEC(p):
    """Atrib : ID INC
             | ID DEC"""
    op = "ADD" if p[2] == "++" else "SUB"
    p[0] = f'PUSHG {p.parser.registers.get(p[1])}\nPUSHI 1\n{op}\nSTOREG {p.parser.registers.get(p[1])}\n'


def p_Atrib_Array(p):
    "Atrib : ID LSQBRACKET Expr RSQBRACKET ATRIB Expr"
    if p[1] in p.parser.registers:
        if p[1] in p.parser.arrays:
            p[0] = f'PUSHGP\nPUSHI {p.parser.registers.get(p[1])[0]}\nPADD\n{p[3]}{p[6]}STOREN\n'
        else:
            print(f"Erro: Variável {p[1]} não é um array.")
            parser.success = False
    else:
        print("Erro: Variável não definida.")
        parser.success = False

# ---------------- Print ----------------
def p_Print_NonFormatted(p):
    "Print : NonFormatted"
    p[0] = p[1]

def p_NonFormatted(p):
    "NonFormatted : PRINT LCPARENT Argument RCPARENT"
    p[0] = p[3]

def p_Argument_String(p):
    "Argument : String"
    p[0] = p[1]

def p_Argument_Expr(p):
    "Argument : Expr"
    p[0] = f'{p[1]}WRITEI\nWRITELN\n'

# ---------------- Expressions ----------------
def p_Expr_Var_Inc(p):
    """Expr : Var
            | ExprIncDec"""
    p[0] = p[1]

def p_Expr_Num(p):
    "Expr : NUM"
    p[0] = f'PUSHI {p[1]}\n'

arith_map = {
    "+": "ADD\n",
    "-": "SUB\n",
    "*": "MUL\n",
    "/": "DIV\n",
    "%": "MOD\n",
}
def p_Expr_Arith(p):
    """Expr : Expr SUM Expr
            | Expr SUB Expr
            | Expr MULT Expr
            | Expr DIV Expr
            | Expr MOD Expr"""
    p[0] = f'{p[1]}{p[3]}{arith_map[p[2]]}'

def p_Expr_Inc_Dec(p):
    """ExprIncDec : ID INC
                  | ID DEC"""
    op = "ADD" if p[2] == "++" else "SUB"
    var_gp_index = p.parser.registers.get(p[1])
    p[0] = f'PUSHG {var_gp_index}\nPUSHI 1\n{op}\nSTOREG {var_gp_index}\nPUSHG {var_gp_index}\n'

# ---------------- Vars -----------------
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

def p_Var_Array(p):
    "Var : ID LSQBRACKET Expr RSQBRACKET"
    if p[1] in p.parser.registers:
        if p[1] not in p.parser.ints:
            p[0] = f'PUSHGP\nPUSHI {p.parser.registers.get(p[1])[0]}\nPADD\n{p[3]}LOADN\n'
        else:
            print(f"Erro: Variável {p[1]} não é um array.")
            parser.success = False
    else:
        print("Erro: Variável não definida.")
        parser.success = False

# ---------------- Input ----------------
def p_Input(p):
    "Input : INPUT LCPARENT String RCPARENT"
    p[0] = f'{p[3]}'

# ---------------- Strings ----------------
def p_String(p):
    "String : QUOTE STRING QUOTE"
    p[0] = f'PUSHS "{p[2]}"\nWRITES\n'

def p_String_Empty(p): 
    "String : Empty"
    p[0] = ''

# ---------------- Errors ----------------
def p_error(p):
    print('Syntax error!\np -> ', p)
    parser.sucesso = False


precedence = (
    ("left", "SUM", "SUB"),
    ("left", "MULT", "DIV", "MOD")
)

tokens = LexerPLC.tokens


lexer = LexerPLC()
parser = yacc.yacc(start="ProgramaInit")

parser.success = True
parser.registers = {}
parser.assembly = ""
parser.gp = 0
parser.ints = []
parser.arrays = []
parser.labels = 0
parser.functions = {}
parser.lineno = 1

with open(f"tests/{sys.argv[1]}.plc") as f:
    content = f.read()

lexer.input(content)
parser.parse(lexer=lexer)

if parser.success:
    print("Ficheiro lido com sucesso")
    with open(f'tests/{sys.argv[1]}.vm', 'w+') as f_out:
        f_out.write(parser.assembly)
        f_out.close()
    print("Código assembly gerado e guardado.")
else:
    print("Erro ao gerar o código.")

