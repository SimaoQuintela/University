/** 
* @file manipulacao_da_stack Módulo que contém as funções responsáveis pela manipulação da stack.
*/

#include <stdio.h>
#include <stdlib.h>
#include "stack.h"  
#include "maths.h"
#include "parser.h"




/**
* \author Hugo Rocha
* \brief Roda para a esquerda os três elementos que estão no topo da stack.
* @param s Passagem da stack como parametro
*/
void rodatres(STACK *s){    // carater @
    DATA x = pop(s);
    DATA y = pop(s);
    DATA z = pop(s);
    push(s, y);
    push(s, x);
    push(s, z);
}

/**
* \author Hugo Rocha
* \brief troca os dois elementos que estão no topo da stack.
* @param s Passagem da stack como parametro
*/
void trocadois(STACK *s){    // carater '\'
    
    DATA x = pop(s);
    DATA y = pop(s);
    push(s, x);
    push(s, y);
}

/**
* \author Hugo Rocha
* \brief duplica o elemento que está no topo da stack.
* @param s Passagem da stack como parametro
*/
void duplica(STACK *s){   // carater _
    DATA x = pop(s);
    push(s, x);
    push(s, x);
}

/**
* \author Hugo Rocha
* \brief remove o elemento que está no topo da stack.
* @param s Passagem da stack como parametro
*/
void popp(STACK *s){    // carater ;
    pop(s);
}

/**
* \author Hugo Rocha
* \brief copia o N-ésimo elemento para o topo da stack.
* @param s Passagem da stack como parametro
*/
void copian(STACK *s){        // carater $
    int x = pop_LONG(s);
    push(s, enesimo(s, x));   // enesimo definida na stack
}

/**
* \author Simão Quintela
* \brief converte o elemento que está no topo da stack para um long.
* @param s Passagem da stack como parametro
*/
void converte_para_long(STACK *s){
    if(has_type(top(s), DOUBLE)){
        double x = pop_DOUBLE(s);
        push_LONG(s, (long)x);
        
    } else if (has_type(top(s), CHAR)){
        char x = pop_CHAR(s);
        push_LONG(s, (long)x);
    }
}

/**
* \author Simão Quintela
* \brief converte o elemento que está no topo da stack para um double.
* @param s Passagem da stack como parametro
*/
void converte_para_double(STACK *s){
    if(has_type(top(s), LONG)){
        long x = pop_LONG(s);
        push_DOUBLE(s, (double)x); 

    } else if (has_type(top(s), CHAR)){
        char x = pop_CHAR(s);
        push_DOUBLE(s, (double)x);
    }
}

/**
* \author Simão Quintela
* \brief converte o elemento que está no topo da stack para um char.
* @param s Passagem da stack como parametro
*/
void converte_para_char(STACK *s){
    if(has_type(top(s), LONG)){
        long x = pop_LONG(s);
        push_CHAR(s, (char)x);

    } else if (has_type(top(s), DOUBLE)){
        double x = pop_DOUBLE(s);
        push_CHAR(s, (char)x);
    }
}

/**
* \author Simão Quintela
* \brief lê uma nova linha e envia-a para o parse2 onde vai ser enviada para o tokenizador para ser interpretada sendo que no fim da sua interpretação não é imprimida.
* @param s Passagem da stack como parametro
* @param letras Passagem das letras como parametro
*/
void ler_linha(STACK *s, STACK *letras){
    char linha[BUFSIZ];
    char *new_line = fgets(linha, BUFSIZ, stdin);

    parse2(s, letras, new_line);
}

/**
* \author Hugo Rocha
* \brief dá push ao valor da letra correspondente para a stack
* @param token Letra que vai ser lida
* @param s Passagem da stack como parametro
* @param letras Passagem das letras como parametro
*/
void variaveis(char token, STACK *s, STACK *letras){
    int i;

    for(i=65; i<=90; i++){
        if(token == i) {
            push(s, letras->stack[i-65]);
        }
    }
}

/**
* \author Hugo Rocha
* \brief Atribuição de valor às letras usadas no comando :letra
* @param c Letra que vai receber o valor do topo da stack
* @param s Passagem da stack como parametro 
* @param letras Passagem das letras como parametro
*/
void atribuivalorvariavel(char c, STACK *s, STACK *letras){
    int i;

    for(i=65; i<=90; i++){
        if(c == i) {
            letras->stack[i-65] = top(s);
        }
    }
}
