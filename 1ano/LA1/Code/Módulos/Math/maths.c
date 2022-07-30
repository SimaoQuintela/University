/**
* @file maths Módulo que contém as funções aritméticas.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <math.h>

#include "maths.h"
#include "stack.h"

/**
* \author Nuno Costa
* \brief Função soma(+) para cada tipo, exceto strings.
* @param s Passagem da stack como parametro
*/ 
void soma(STACK *s){    
    if(has_type(top(s), LONG) && has_type(penultimo(s), LONG)){
        long x = pop_LONG(s);       // x long
        long y = pop_LONG(s);       // y long

        push_LONG(s, x+y);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), DOUBLE)){
        double x = pop_DOUBLE(s);   // x double
        double y = pop_DOUBLE(s);   // y double

        push_DOUBLE(s, x+y);

    } else if(has_type(top(s), LONG) && has_type(penultimo(s), DOUBLE)){
        long x = pop_LONG(s);       // x long
        double y = pop_DOUBLE(s);   // y double

        double result = (double)x + y;  
        push_DOUBLE(s, result);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), LONG)){
        double x = pop_DOUBLE(s);   // x double
        long y =  pop_LONG(s);      // y long

        double result = x + (double)y;
        push_DOUBLE(s, result);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), CHAR)){
        char x = pop_CHAR(s);       // x char
        char y = pop_CHAR(s);       // y char

        long result = (long)x + (long)y;
        push_LONG(s, result);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), LONG)){
        char x = pop_CHAR(s);       // x char
        long y = pop_LONG(s);       // y long 

        long result = (long)x + y;
        push_LONG(s, result);

    } else if(has_type(top(s), LONG) && has_type(penultimo(s), CHAR)){
        long x = pop_LONG(s);       // x long
        char y = pop_CHAR(s);       // y char

        long result = x + (long)y;
        push_LONG(s, result);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), DOUBLE)){
        char x = pop_CHAR(s);       // x char 
        double y = pop_DOUBLE(s);   // y double

        double result = (double)x + y;
        push_DOUBLE(s, result);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), CHAR)){
        double x = pop_DOUBLE(s);   // x double 
        char y = pop_CHAR(s);       // y char

        double result = x + (double)y;
        push_DOUBLE(s, result);
    } else if(has_type(top(s), LONG) && has_type(penultimo(s), STRING)){
        long x = pop_LONG(s);
        char* y = pop_STRING(s);

        char* x2 = x + "\0";

        push_STRING(s, strcat(y,x2));
    } else if(has_type(top(s), STRING) && has_type(penultimo(s), STRING)){
        char* x = pop_STRING(s);
        char* y = pop_STRING(s);

        char* r = calloc(1, sizeof(char)* (tamanho(x) + tamanho(y)));
        strcpy(r, y);

        push_STRING(s, strcat(r,x));
    } else if(has_type(top(s), arrays) && (has_type(penultimo(s), CHAR) || has_type(penultimo(s), LONG) || has_type(penultimo(s), DOUBLE) )){
        struct stack* x = pop_arrays(s);
        DATA y = pop(s);

        int i = x->n_elems;
        push(x, x->stack[i-1]);
        i--;
        while(i > 0){
            x->stack[i] = x->stack[i -1];
            i--;
        }
       
        x->stack[0] = y;

        push_arrays(s, x);
    } else if(has_type(top(s), arrays) && (has_type(penultimo(s), CHAR) || has_type(penultimo(s), LONG) || has_type(penultimo(s), DOUBLE) )){
        struct stack* x = pop_arrays(s);
        DATA y = pop(s);

        push(x, y);

        push_arrays(s, x);
    } else if(has_type(top(s), LONG) && has_type(penultimo(s), arrays)){
        long x = pop_LONG(s);
        struct stack* array = pop_arrays(s);

        push_LONG(array, x);
        push_arrays(s, array);
    } else if(has_type(top(s), arrays) && has_type(penultimo(s), arrays)){
        struct stack* array1 = pop_arrays(s);   // juntar 1 ao 2
        struct stack* array2 = pop_arrays(s);

        int i = 0;
        while(i < array1->n_elems){
            push(array2,array1->stack[i]); 
            i++;
        }

        push_arrays(s, array2);
    }

}


/**
* \author Simão Quintela
* \brief Função subtração(-) para cada tipo, exceto strings.
* @param s Passagem da stack como parametro
*/ 
void subtrai(STACK *s){

if(has_type(top(s), LONG) && has_type(penultimo(s), LONG)){
        long x = pop_LONG(s);       // x long
        long y = pop_LONG(s);       // y long

        push_LONG(s, y-x);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), DOUBLE)){
        double x = pop_DOUBLE(s);   // x double
        double y = pop_DOUBLE(s);   // y double

        push_DOUBLE(s, y-x);

    } else if(has_type(top(s), LONG) && has_type(penultimo(s), DOUBLE)){
        long x = pop_LONG(s);       // x long
        double y = pop_DOUBLE(s);   // y double

        double result = y - (double)x ;  
        push_DOUBLE(s, result);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), LONG)){
        double x = pop_DOUBLE(s);   // x double
        long y =  pop_LONG(s);      // y long

        double result = (double)y - x;
        push_DOUBLE(s, result);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), CHAR)){
        char x = pop_CHAR(s);       // x char
        char y = pop_CHAR(s);       // y char

        long result = (long)y - (long)x;
        push_LONG(s, result);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), LONG)){
        char x = pop_CHAR(s);       // x char
        long y = pop_LONG(s);       // y long 

        long result = y- (long)x;
        push_LONG(s, result);

    } else if(has_type(top(s), LONG) && has_type(penultimo(s), CHAR)){
        long x = pop_LONG(s);       // x long
        char y = pop_CHAR(s);       // y char

        long result = (long)y - x;
        push_LONG(s, result);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), DOUBLE)){
        char x = pop_CHAR(s);       // x char 
        double y = pop_DOUBLE(s);   // y double

        double result =  y - (double)x;
        push_DOUBLE(s, result);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), CHAR)){
        double x = pop_DOUBLE(s);   // x double 
        char y = pop_CHAR(s);       // y char

        double result = (double)y - x;
        push_DOUBLE(s, result);
    }
}


/**
* \author Simão Quintela
* \brief Função multiplicação(*) para cada tipo, exceto strings.
* @param s Passagem da stack como parametro
*/ 
void multiplica(STACK *s){
    if(has_type(top(s), LONG) && has_type(penultimo(s), LONG)){
        long x = pop_LONG(s);       // x long
        long y = pop_LONG(s);       // y long

        push_LONG(s, x*y);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), DOUBLE)){
        double x = pop_DOUBLE(s);   // x double
        double y = pop_DOUBLE(s);   // y double

        push_DOUBLE(s, x*y);

    } else if(has_type(top(s), LONG) && has_type(penultimo(s), DOUBLE)){
        long x = pop_LONG(s);       // x long
        double y = pop_DOUBLE(s);   // y double

        double result = (double)x * y;  
        push_DOUBLE(s, result);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), LONG)){
        double x = pop_DOUBLE(s);   // x double
        long y =  pop_LONG(s);      // y long

        double result = x * (double)y;
        push_DOUBLE(s, result);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), CHAR)){
        char x = pop_CHAR(s);       // x char
        char y = pop_CHAR(s);       // y char

        long result = (long)x * (long)y;
        push_LONG(s, result);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), LONG)){
        char x = pop_CHAR(s);       // x char
        long y = pop_LONG(s);       // y long 

        long result = (long)x * y;
        push_LONG(s, result);

    } else if(has_type(top(s), LONG) && has_type(penultimo(s), CHAR)){
        long x = pop_LONG(s);       // x long
        char y = pop_CHAR(s);       // y char

        long result = x * (long)y;
        push_LONG(s, result);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), DOUBLE)){
        char x = pop_CHAR(s);       // x char 
        double y = pop_DOUBLE(s);   // y double

        double result = (double)x * y;
        push_DOUBLE(s, result);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), CHAR)){
        double x = pop_DOUBLE(s);   // x double 
        char y = pop_CHAR(s);       // y char

        double result = x * (double)y;
        push_DOUBLE(s, result);
    } else if(has_type(top(s), LONG) && has_type(penultimo(s), STRING)){
        long x = pop_LONG(s);
        char *s1 = pop_STRING(s);
        int i;
        int j;
        int k = 0;

        char *resultado = malloc((((tamanho(s1))*x)+1)*(sizeof(char)));

        for(i=0; i<(tamanho(s1)); i++){
            resultado[i] = s1[i];
        }
        
        for(j=i; j<((tamanho(s1)) * x); j++) {
             resultado[j] = resultado[k];
             k++;
        }
        resultado[(tamanho(s1)*x)] = '\0';

        push_STRING(s, resultado);

    } else if(has_type(top(s), LONG) && has_type(penultimo(s), arrays)){
        long n = pop_LONG(s);
        struct stack* array = pop_arrays(s);

        long i;
        long k = 0;
        long tam = array->n_elems;


        for(i=0; i<((n-1)*tam); i++){
            if(array->size == array->n_elems){
                array->size += 100;
                array->stack = (DATA *) realloc(array->stack, array->size * sizeof(DATA));
            }
            array->stack[array->n_elems] = array->stack[k];
            k++;
            array->n_elems++;

        }


        push_arrays(s, array);

    } 

}

/**
* \author Hugo Rocha
* \brief Função divisão(/) para cada tipo, exceto strings.
* @param s Passagem da stack como parametro
*/ 
void dividir(STACK *s){
 if(has_type(top(s), LONG) && has_type(penultimo(s), LONG)){
        long x = pop_LONG(s);       // x long
        long y = pop_LONG(s);       // y long
        assert(x != 0);

        push_LONG(s, y / x);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), DOUBLE)){
        double x = pop_DOUBLE(s);   // x double
        double y = pop_DOUBLE(s);   // y double
        assert(x != 0);             

        push_DOUBLE(s, y / x);

    } else if(has_type(top(s), LONG) && has_type(penultimo(s), DOUBLE)){
        long x = pop_LONG(s);       // x long
        double y = pop_DOUBLE(s);   // y double
    //    assert(x != 0);  

        double result = y / x;  
        push_DOUBLE(s, result);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), LONG)){
        double x = pop_DOUBLE(s);   // x double
        long y =  pop_LONG(s);      // y long
        assert(x != 0);     

        double result = y / (double)x;
        push_DOUBLE(s, result);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), CHAR)){
        char x = pop_CHAR(s);       // x char
        char y = pop_CHAR(s);       // y char
        assert(x != 0);       

        long result = (long)y / (long)x;
        push_LONG(s, result);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), LONG)){
        char x = pop_CHAR(s);       // x char
        long y = pop_LONG(s);       // y long
        assert(x != 0);       

        long result = (long)y / x;
        push_LONG(s, result);

    } else if(has_type(top(s), LONG) && has_type(penultimo(s), CHAR)){
        long x = pop_LONG(s);       // x long
        char y = pop_CHAR(s);       // y char
        assert(x != 0);   

        long result = y / (long)x;
        push_LONG(s, result);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), DOUBLE)){
        char x = pop_CHAR(s);       // x char 
        double y = pop_DOUBLE(s);   // y double
        assert(x != 0);   

        double result = (double)y / x;
        push_DOUBLE(s, result);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), CHAR)){
        double x = pop_DOUBLE(s);   // x double 
        char y = pop_CHAR(s);       // y char   
        assert(x != 0);

        double result = y / (double)x;
        push_DOUBLE(s, result);
    } else if(has_type(top(s), STRING) && has_type(penultimo(s), STRING)){
        char *string_a_comparar = pop_STRING(s);
        char *string_com_substrings = pop_STRING(s);

        struct stack* array = new_stack();

        char *token;

        while(*string_com_substrings != '\0'){
            token = strtok(string_com_substrings, string_a_comparar);
            push_STRING(array, token);


            string_com_substrings += tamanho(token) + tamanho(string_a_comparar);   // função do maths

        }

        push_arrays(s, array);
    }
}

/**
* \author Hugo Rocha
* \brief Função responsável por decrementar(() 1 unidade para cada tipo, exceto strings.
* @param s Passagem da stack como parametro
*/ 
void decrementa(STACK *s){
 if(has_type(top(s), LONG)){
        long x = pop_LONG(s);       // x long
        push_LONG(s, x - 1);

    } else if(has_type(top(s), DOUBLE)){
        double x = pop_DOUBLE(s);   // x double
        push_DOUBLE(s, x - 1);

    } else if(has_type(top(s), CHAR)){
        char x = pop_CHAR(s);       // x char

        push_CHAR(s, x-1);
    } else if(has_type(top(s), arrays)){            // [ 1 2 3 ] (
        struct stack* arrays = pop_arrays(s);

        DATA x = arrays->stack[0];

        int i = 0;
        while(i < arrays->n_elems -1){
            arrays->stack[i] = arrays->stack[i+1];
            i++; 
        }
        pop(arrays);
        push_arrays(s, arrays);
        push(s, x); 
    } else if(has_type(top(s), STRING)){        
        char *string = pop_STRING(s);
        char x = *string;
        string++;

        push_STRING(s, string);
        push_CHAR(s, x);
    }
}
/**
* \author Hugo Rocha
* \brief Função responsável por incrementar()) 1 unidade para cada tipo, exceto strings.
* @param s Passagem da stack como parametro
*/ 
void incrementa(STACK *s){
  if(has_type(top(s), LONG)){
        long x = pop_LONG(s);       // x long
        push_LONG(s, x + 1);

    } else if(has_type(top(s), DOUBLE)){
        double x = pop_DOUBLE(s);   // x double
        push_DOUBLE(s, x + 1);

    } else if(has_type(top(s), CHAR)){
        char x = pop_CHAR(s);       // x char

        push_CHAR(s, x + 1);
    } else if(has_type(top(s), arrays)){            // [ 1 2 3 ] )
        struct stack* arrays = pop_arrays(s);

        DATA x = pop(arrays);
        push_arrays(s, arrays);
        push(s, x);
    
    } else if(has_type(top(s), STRING)){        
        char *string = pop_STRING(s);
        char x = string[tamanho(string)-1];
        
        string[tamanho(string)-1] = '\0';

        push_STRING(s, string);
        push_CHAR(s, x);
    }
}
/**
* \author Nuno Costa
* \brief Função módulo(%) para cada tipo, exceto strings e doubles.
* @param s Passagem da stack como parametro
*/ 
void modulo(STACK *s){
    if(has_type(top(s), LONG) && has_type(penultimo(s), LONG)){
        long x = pop_LONG(s);       // x long
        long y = pop_LONG(s);       // y long
        assert(x != 0);

        push_LONG(s, y%x);
    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), CHAR)){
        char x = pop_CHAR(s);       // x char
        char y = pop_CHAR(s);       // y char
        assert(x != 0);

        long result =  (long)y % (long)x;
        push_LONG(s, result);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), LONG)){
        char x = pop_CHAR(s);       // x char
        long y = pop_LONG(s);       // y long 
        assert(x != 0);

        long result = y % (long)x;
        push_LONG(s, result);

    } else if(has_type(top(s), LONG) && has_type(penultimo(s), CHAR)){
        long x = pop_LONG(s);       // x long
        char y = pop_CHAR(s);       // y char
        assert(x != 0);

        long result = (long)y % x;
        push_LONG(s, result);
    }
}


/**
* \author Tiago Guedes
* \brief Função expoente(#) para cada tipo, exceto strings.
* @param s Passagem da stack como parametro
*/ 
void expoente(STACK *s){
    if(has_type(top(s), LONG) && has_type(penultimo(s), LONG)){
        long x = pop_LONG(s);       // x long
        long y = pop_LONG(s);       // y long

        push_LONG(s, pow(y,x));

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), DOUBLE)){
        double x = pop_DOUBLE(s);   // x double
        double y = pop_DOUBLE(s);   // y double

        push_DOUBLE(s, pow(y,x));

    } else if(has_type(top(s), LONG) && has_type(penultimo(s), DOUBLE)){
        long x = pop_LONG(s);       // x long
        double y = pop_DOUBLE(s);   // y double

        double result = pow(y,(double)x);  
        push_DOUBLE(s, result);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), LONG)){
        double x = pop_DOUBLE(s);   // x double
        long y =  pop_LONG(s);      // y long

        double result = pow((double)y,x);
        push_DOUBLE(s, result);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), CHAR)){
        char x = pop_CHAR(s);       // x char
        char y = pop_CHAR(s);       // y char

        long result = pow((long)y,(long)x);
        push_LONG(s, result);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), LONG)){
        char x = pop_CHAR(s);       // x char
        long y = pop_LONG(s);       // y long 

        long result = pow(y,(long)x);
        push_LONG(s, result);

    } else if(has_type(top(s), LONG) && has_type(penultimo(s), CHAR)){
        long x = pop_LONG(s);       // x long
        char y = pop_CHAR(s);       // y char

        long result = pow((long)y,x);
        push_LONG(s, result);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), DOUBLE)){
        char x = pop_CHAR(s);       // x char 
        double y = pop_DOUBLE(s);   // y double

        double result = pow(y,(double)x);
        push_DOUBLE(s, result);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), CHAR)){
        double x = pop_DOUBLE(s);   // x double 
        char y = pop_CHAR(s);       // y char

        double result = pow((double)y,x);
        push_DOUBLE(s, result);
    } else if(has_type(top(s), STRING) && has_type(penultimo(s), STRING)){
        char* s1 = pop_STRING(s);
        char* s2 = pop_STRING(s);

        push_LONG(s, mystrstr(s2, s1));
    }
}


/**
* \author Tiago Guedes
* \brief Função "e"(&) responsável por determinar a interseção de bits entre dois números inteiros.
* @param s Passagem da stack como parametro
*/ 
void e(STACK *s){
    if(has_type(top(s), LONG) && has_type(penultimo(s), LONG)){
        long x = pop_LONG(s);       // x long
        long y = pop_LONG(s);       // y long

        push_LONG(s, y & x);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), CHAR)){
        char x = pop_CHAR(s);       // x char
        char y = pop_CHAR(s);       // y char

        long result = (long)y & (long)x;
        push_LONG(s, result);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), LONG)){
        char x = pop_CHAR(s);       // x char
        long y = pop_LONG(s);       // y long

        long result = (long)y & x;
        push_LONG(s, result);

    } else if(has_type(top(s), LONG) && has_type(penultimo(s), CHAR)){
        long x = pop_LONG(s);       // x long
        char y = pop_CHAR(s);       // y char

        long result = y & (long)x;
        push_LONG(s, result);
    }
}

/**
* \author Tiago Guedes
* \brief Função "ou"(|) responsável por determinar a reunião de bits entre dois números inteiros.
* @param s Passagem da stack como parametro
*/ 
void ou(STACK *s){
    if(has_type(top(s), LONG) && has_type(penultimo(s), LONG)){
        long x = pop_LONG(s);       // x long
        long y = pop_LONG(s);       // y long

        push_LONG(s, y | x);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), CHAR)){
        char x = pop_CHAR(s);       // x char
        char y = pop_CHAR(s);       // y char

        long result = (long)y | (long)x;
        push_LONG(s, result);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), LONG)){
        char x = pop_CHAR(s);       // x char
        long y = pop_LONG(s);       // y long

        long result = (long)y | x;
        push_LONG(s, result);

    } else if(has_type(top(s), LONG) && has_type(penultimo(s), CHAR)){
        long x = pop_LONG(s);       // x long
        char y = pop_CHAR(s);       // y char

        long result = y | (long)x;
        push_LONG(s, result);
    }
}

/**
* \author Paulo Vasconcelos
* \brief Função xor(^) responsável por colocar a 0 todos os bits em comum e a 1 todos os bits diferentes entre si, de dois números e calcular o seu resultado.
* @param s Passagem da stack como parametro
*/ 
void xorr(STACK *s){
 if(has_type(top(s), LONG) && has_type(penultimo(s), LONG)){
        long x = pop_LONG(s);       // x long
        long y = pop_LONG(s);       // y long

        push_LONG(s, y ^ x);
    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), CHAR)){
        char x = pop_CHAR(s);       // x char
        char y = pop_CHAR(s);       // y char

        long result = (long)y ^ (long)x;
        push_LONG(s, result);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), LONG)){
        char x = pop_CHAR(s);       // x char
        long y = pop_LONG(s);       // y long

        long result = (long)y ^ x;
        push_LONG(s, result);

    } else if(has_type(top(s), LONG) && has_type(penultimo(s), CHAR)){
        long x = pop_LONG(s);       // x long
        char y = pop_CHAR(s);       // y char

        long result = y ^ (long)x;
        push_LONG(s, result);
    }
}
/**
* \author Paulo Vasconcelos
* \brief Função nott responsável por inverter todos os bits de um número inteiro
* @param s Passagem da stack como parametro
*/ 
void nott(STACK *s){
  	if(has_type(top(s), LONG)){
        long x = pop_LONG(s);       // x long
        push_LONG(s, ~x);

    } else if(has_type(top(s), CHAR)){
        char x = pop_CHAR(s);       // x char
        long y = (long)x;

        push_LONG(s, ~y);
    } else if(has_type(top(s), arrays)){
    	struct stack* x = pop_arrays(s);
        int index = 0;

		while (x->n_elems != index) {
		    push(s, x->stack[index]);
            index++;	
		}
    } else if(has_type(top(s), STRING)){
        char* string = pop_STRING(s);
        int index = 0;

        while ((tamanho(string)) != index) {
            if(string[index] >= '0' && string[index] <= '9'){
                push_LONG(s, (long)string[index] -48);
            } else {
                push_CHAR(s, string[index]);
            }
            index++;    
        }

    }

}



// comando #
/**
* @param v String que vai ser avaliada
* @returns Devolve o tamanho da string
*/
int tamanho(char v[]){
    int i;


    for(i=0; v[i] != '\0'; i++) ;

    return i;
}

/**
*
* @param s1 String passada como parametro
* @param i Indice da string s1
* @param tam Tamanho da string 
* @param result String resultante
* @returns Retorna uma string
*/
void cria_string(char s1[], int i, int tam, char result[]){
    int j;
    
    for(j=0; j<tam; j++){
      result[j] = s1[i];
      i++;
    }

    result[tam] = '\0';


 }




/**
* @param s1 String passada como parâmetro
* @param s2 String passada como parâmetro
* @returns Devolve a posicao em que s2 aparece em s1.
*/
int mystrstr(char s1[], char s2[]){
  int j = -1;
  int i;
  char aux[tamanho(s2)];

  for(i=0; i<=(tamanho(s1) - tamanho(s2)); i++){
    cria_string(s1, i, tamanho(s2), aux);
    if(strcmp(aux, s2) == 0  ){
       return i;
    }
  }
  
  return j;
}
