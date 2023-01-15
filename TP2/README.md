
# Syntax
### All of these operators and flux control instructions are already implemented

* **Declarations**
    * int x
    * int x = 10
    * int x[n]
    * int x[n][m]

* **Comparison**  
    * x **<=** y
    * x **>=** y
    * x **<** y
    * x **<** y
    * x **==** y

* **Numeric Operations**  
    * x **+** y
    * x **-** y
    * x **/** y
    * x **\*** y
    * x **%** y
    * x **++**
    * y **--**
* **Logical operations**
    * x **and** y 
    * x **or** y
* **Ifs**
    * If(conditions):
    * else:
    * elif(conditions):

* **Cycles**
    * do:  
    &nbsp;&nbsp;&nbsp; ...  
    &nbsp;&nbsp;&nbsp; ...  
    while(conditions):

* **Input/Output**
    * int x = input()
    * int x = input("Declare the variable with the value: ")
    * x = input()
    * x = input("Update the variable name with the value: ")
    * print("David's beautiful green eyes") 

**GIC**
```
ProgramaInit : Programa ENDMARKER
Programa : Decls Corpo
         | Corpo
Decls    : Decl
         | Decls Decl
Decl     : INTDec ID
         | INTDec ID ATRIB NUM
         | INTDec ID ATRIB Input 
         | INTDec ID ATRIB INPUT LCBRACKET String RCBRACKET
         | INTDec ID LSQBRACKET NUM RSQBRACKET
Corpo    : Proc Newline
         | Corpo Proc Newline
         | Newline
Newline  : NEWLINE
         | ε
Proc     : Atrib
         | Print
         | If
         | Cycle
         | Call
Cycle    : DoWhile
         | While
Call     : CALL
Print    : NonFormatted
         | Formatted (not implemented)
NonFormatted : PRINT LCPARENT QUOTE Argument QUOTE RCPARENT
Formatted : ....
Argument : String
         | Expr


If       : IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent
         | IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent ELSE COLON Newline INDENT Corpo DEDENT

DoWhile  : DO COLON Newline INDENT Corpo Dedent WHILE LCPARENT Cond RCPARENT NEWLINE

While    : WHILE LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent

Atrib    : ID ATRIB Expr
         | ID ATRIB Input
         | ID INC
         | ID DEC
Cond     : Expr GT Expr 
         | Expr LT Expr
         | Expr GEQ Expr
         | Expr LEQ Expr
         | Expr EQUIV Expr
         | Expr NEQ Expr
         | Cond OR Cond
         | Cond AND Cond
         | NOT Cond

Expr     : Var                
         | NUM                
         | ID INC             
         | ID DEC             
         | Expr SUM Expr      
         | Expr SUB Expr      
         | Expr DIV Expr      
         | Expr MUL Expr      
         | Expr MOD Expr      

Var      : ID
Input    : INPUT LCPARENT String RCPARENT
String   : QUOTE STRING QUOTE
         | ε

```
