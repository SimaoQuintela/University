
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


**GIC**
```
Programa : Decls Corpo
         | Corpo
Decls    : Decl
         | Decls Decl
Decl     : INTDec ID ATR NUM
         | INTDec NUM
         | INTDec ID LSQBRACKET NUM RSQBRACKET
         | INTDec ID LSQBRACKET NUM RSQBRACKET LSQBRACKET NUM RSQBRACKET
Corpo    : Proc
         | Corpo Proc
Proc     : Print
         | If
         | Cycle
         | Input

```
