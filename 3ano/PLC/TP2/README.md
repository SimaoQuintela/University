# Welcome to Python-Like-C
### Python-Like-C was developed to take what's best in Python and add a bit of C operators and procedures that we think are missing in Python, like ++/--, do while loops, etc. 
# Syntax
### All of these operators and flux control instructions are already implemented

* **Declarations**
    * int x
    * int x = 10
    * int x[4]
    * int x[4] = {10,20,30,40}

* **Comparison**  
    * x **<=** y
    * x **>=** y
    * x **<** y
    * x **<** y
    * x **==** y
    * x **/=** y

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
    * **not** x
* **Ifs**
    * If(conditions):
    &nbsp;&nbsp;&nbsp; ...  
    * else:

* **Cycles**
    * do:  
    &nbsp;&nbsp;&nbsp; ...  
    &nbsp;&nbsp;&nbsp; ...  
    while(conditions)
    * while(cond):
    &nbsp;&nbsp;&nbsp; ...  
    &nbsp;&nbsp;&nbsp; ...  

* **Input/Output**
    * int x = input()
    * int x = input("Declare the variable with the value: ")
    * x = input()
    * x = input("Update the variable name with the value: ")
    * print("David's beautiful green eyes") 

* **Functions**
   * def name( ): - no parameters yet 

* **Assertion**
   * assert(cond)
   
## **We also implemented Python indentation. Hope you notice that :wink:**

**GIC**
```
ProgramaInit : Programa ENDMARKER
Programa : Decls Corpo
         | Corpo
Decls    : Decl Newline
         | Decls Decl Newline
Decl     : INTDec ID
         | INTDec ID ATRIB NUM
         | INTDec ID ATRIB Input 
         | INTDec ID LSQBRACKET NUM RSQBRACKET
         | INTDec ID LSQBRACKET NUM RSQBRACKET ATRIB ArrayValues
         | Def
Def      : DEF ID COLON Newline INDENT Corpo DEDENT
         | DEF ID COLON Newline INDENT Decls Corpo DEDENT
ArrayValues : LCURLBRACKET ArrayIntValues RCURLBRACKET
ArrayIntValues : ArrayIntValues ',' Expr
               | Expr
Corpo    : Proc Newline
         | Corpo Proc Newline
         | Newline
Newline  : NEWLINE
         | ε
Dedent   : Dedent DEDENT
         | ε
Proc     : Atrib
         | Print
         | If
         | Cycle
         | Call
Cycle    : DoWhile
         | While
Call     : CALL

If       : IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent
         | IF LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent ELSE COLON Newline INDENT Corpo DEDENT

DoWhile  : DO COLON Newline INDENT Corpo Dedent WHILE LCPARENT Cond RCPARENT NEWLINE

While    : WHILE LCPARENT Cond RCPARENT COLON Newline INDENT Corpo Dedent

Atrib    : ID ATRIB Expr
         | ID ATRIB Input
         | ID INC
         | ID DEC
         | ID LSQBRACKET Expr RSQBRACKET ATRIB Expr
Cond     : Expr GT Expr 
         | Expr LT Expr
         | Expr GEQ Expr
         | Expr LEQ Expr
         | Expr EQUIV Expr
         | Expr NEQ Expr
         | Expr OR Expr
         | Expr AND Expr
         | NOT Cond

Expr     : Var                
         | NUM
         | ExprIncDec         
         | ID INC             
         | ID DEC             
         | Expr SUM Expr      
         | Expr SUB Expr      
         | Expr DIV Expr      
         | Expr MUL Expr      
         | Expr MOD Expr      

ExprIncDec : ID INC
           | ID DEC

Var      : ID
         | ID LSQBRACKET Expr RSQBRACKET
Print    : NonFormatted
NonFormatted : PRINT LCPARENT QUOTE Argument QUOTE RCPARENT
Argument : String
         | Expr
Input    : INPUT LCPARENT String RCPARENT
String   : QUOTE STRING QUOTE
         | ε

```
