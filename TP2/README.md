
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
Programa : Decls Corpo
         | Corpo
Decls    : Decl
         | Decls Decl
Decl     : INTDec ID
         | INTDec ID ATRIB NUM
         | INTDec ID ATRIB Input 
         | INTDec ID ATRIB INPUT LCBRACKET RCBRACKET
         | INTDec ID LSQBRACKET NUM RSQBRACKET
         | INTDec ID LSQBRACKET NUM RSQBRACKET LSQBRACKET NUM RSQBRACKET
Input    : INPUT LCPARENT String RCPARENT
String   : QUOTE STRING QUOTE
         | ε
Corpo    : Proc
         | Corpo Proc
Proc     : Atrib
         | Print
         | If
         | Cycle
Print    : NonFormatted
         | Formatted (not implemented)
NonFormatted : PRINT LCPARENT QUOTE STRING QUOTE RCPARENT
Formatted : ....

Atrib    : UpdateVar
         | Input
         | ....
         | ....
Expr     : ID SUM SUM
         | ID SUB SUB
         | ID SUM ATRIB NUM
         | ID SUB ATRIB
         | ....
         | .... 


```
