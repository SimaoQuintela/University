/** 
* @file main ficheiro que contém a função main.
* \author Simão Quintela
*/

#include <stdio.h>
#include "parser.h"
#include "stack.h"
/**
* \brief A função main inicializa a stack e as letras passando-as como parametro ao fgets que é passado como parametro juntamente com a stack e as letras para o parse.
*/
int main() {
  char buf[BUFSIZ];
  STACK *s = new_stack();
  STACK *letras = new_stack();
  preencheLetras(letras);
  
  parse(s, letras, fgets(buf, BUFSIZ, stdin));
  return 0;
}
