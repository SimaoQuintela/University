#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "stack.h"
#include "manipulacao_da_stack.h"
#include "arrays.h"
#include "maths.h"

// , 
/**
* @param s Stack passada como parâmetro
*/
void range_array (STACK *s) {
    if(has_type(top(s), LONG)){
        long x = pop_LONG(s);
        long i = 0;
        struct stack* array = new_stack();
        
        while(i<x){
        	push_LONG(array, i);	    
        	i++;
        }
        push_arrays(s, array);

    } else if(has_type(top(s), arrays)){
        struct stack* array = pop_arrays(s);

        push_LONG(s, array->n_elems);
    } else if(has_type(top(s), STRING)){
        char* stg = pop_STRING(s);

        push_LONG(s, tamanho(stg));
    }
}


//    S/
/**
* @param s Stack passada como parâmetro
*/
void separa_por_espaco(STACK *s){
	char *input = pop_STRING(s);

	char *delims = " ";
	struct stack* array = new_stack();
	char *token;

	while(*input != '\0'){
		token = strtok(input, delims);
		push_STRING(array, token);

		input += tamanho(token) + 1;	// função do maths
	}

	push_arrays(s, array);
}

