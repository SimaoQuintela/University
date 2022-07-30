/**
* @file logica Modulo que contem as funções lógicas
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "stack.h"
#include "logica.h"


/**
* @param s Passagem da stack como parametro
*/
void emaior(STACK *s){
    if(has_type(top(s), LONG) && has_type(penultimo(s), LONG)){
        long x = pop_LONG(s);
        long y = pop_LONG(s);
            
        if (x>=y) push_LONG(s, x);
        else push_LONG(s, y);


    } else if(has_type(top(s), LONG) && has_type(penultimo(s), DOUBLE)){
        long x = pop_LONG(s);
        double y = pop_DOUBLE(s);
            
        if (x>=y) push_LONG(s, x);
        else push_DOUBLE(s, y);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), LONG)){
        double x = pop_DOUBLE(s);
        long y = pop_LONG(s);
            
        if (x>=y) push_DOUBLE(s, x);
        else push_LONG(s, y);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), DOUBLE)){
        double x = pop_DOUBLE(s);
        double y = pop_DOUBLE(s);
            
        if (x>=y) push_DOUBLE(s, x);
        else push_DOUBLE(s, y);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), CHAR)){
        char x = pop_CHAR(s);
        char y = pop_CHAR(s);
            
        if (x>=y) push_CHAR(s, x);
        else push_CHAR(s, y);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), LONG)){
        char x = pop_CHAR(s);
        long y = pop_LONG(s);
            
        if (x>=y) push_CHAR(s, x);
        else push_LONG(s, y);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), DOUBLE)){
        char x = pop_CHAR(s);
        double y = pop_DOUBLE(s);
            
        if (x>=y) push_CHAR(s, x);
        else push_DOUBLE(s, y);

    }  else if(has_type(top(s), LONG) && has_type(penultimo(s), CHAR)){
        long x = pop_LONG(s);
        char y = pop_CHAR(s);
            
        if (x>=y) push_LONG(s, x);
        else push_CHAR(s, y);

    }  else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), CHAR)){
        double x = pop_DOUBLE(s);
        char y = pop_CHAR(s);
            
        if (x>=y) push_DOUBLE(s, x);
        else push_CHAR(s, y);
    
    }   else if(has_type(top(s), STRING) && has_type(penultimo(s), STRING)){
            char *s1 = pop_STRING(s);
            char *s2 = pop_STRING(s);

            if(strcmp(s2, s1) > 0){
                push_STRING(s, s2);
            } else 
                push_STRING(s, s1);
        }
}


/**
* @param s Passagem da stack como parametro
*/
void emenor(STACK *s){
     if(has_type(top(s), LONG) && has_type(penultimo(s), LONG)){
        long x = pop_LONG(s);
        long y = pop_LONG(s);
            
        if (x>=y) push_LONG(s, y);
        else push_LONG(s, x);


    } else if(has_type(top(s), LONG) && has_type(penultimo(s), DOUBLE)){
        long x = pop_LONG(s);
        double y = pop_DOUBLE(s);
            
        if (x>=y) push_DOUBLE(s, y);
        else push_LONG(s, x);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), LONG)){
        double x = pop_DOUBLE(s);
        long y = pop_LONG(s);
            
        if (x>=y) push_LONG(s, y);
        else push_DOUBLE(s, x);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), DOUBLE)){
        double x = pop_DOUBLE(s);
        double y = pop_DOUBLE(s);
            
        if (x>=y) push_DOUBLE(s, y);
        else push_DOUBLE(s, x);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), CHAR)){
        char x = pop_CHAR(s);
        char y = pop_CHAR(s);
            
        if (x>=y) push_CHAR(s, y);
        else push_CHAR(s, x);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), LONG)){
        char x = pop_CHAR(s);
        long y = pop_LONG(s);
            
        if (x>=y) push_LONG(s, y);
        else push_CHAR(s, x);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), DOUBLE)){
        char x = pop_CHAR(s);
        double y = pop_DOUBLE(s);
            
        if (x>=y) push_DOUBLE(s, y);
        else push_CHAR(s, x);

    }  else if(has_type(top(s), LONG) && has_type(penultimo(s), CHAR)){
        long x = pop_LONG(s);
        char y = pop_CHAR(s);
            
        if (x>=y) push_CHAR(s, y);
        else push_LONG(s, x);

    }  else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), CHAR)){
        double x = pop_DOUBLE(s);
        char y = pop_CHAR(s);
            
        if (x>=y) push_CHAR(s, y);
        else push_DOUBLE(s, x);

    }   else if(has_type(top(s), STRING) && has_type(penultimo(s), STRING)){
            char *s1 = pop_STRING(s);
            char *s2 = pop_STRING(s);

            if(strcmp(s2, s1) > 0){
                push_STRING(s, s1);
            } else 
              push_STRING(s, s2);
        }
}


/**
* @param s Passagem da stack como parametro
*/
void igual(STACK *s){
     if(has_type(top(s), LONG) && has_type(penultimo(s), LONG)){
        long x = pop_LONG(s);
        long y = pop_LONG(s);
            
        if (x==y) push_LONG(s, 1);
        else push_LONG(s, 0);


    } else if(has_type(top(s), LONG) && has_type(penultimo(s), DOUBLE)){
        long x = pop_LONG(s);
        double y = pop_DOUBLE(s);
            
        if (x==y) push_LONG(s, 1);
        else push_LONG(s, 0);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), LONG)){
        double x = pop_DOUBLE(s);
        long y = pop_LONG(s);
            
        if (x==y) push_LONG(s, 1);
        else push_LONG(s, 0);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), DOUBLE)){
        double x = pop_DOUBLE(s);
        double y = pop_DOUBLE(s);
            
        if (x==y) push_LONG(s, 1);
        else push_LONG(s, 0);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), CHAR)){
        char x = pop_CHAR(s);
        char y = pop_CHAR(s);
            
        if (x==y) push_LONG(s, 1);
        else push_LONG(s, 0);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), LONG)){
        char x = pop_CHAR(s);
        long y = pop_LONG(s);
            
        if (x==y) push_CHAR(s, 1);
        else push_LONG(s, 0);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), DOUBLE)){
        char x = pop_CHAR(s);
        double y = pop_DOUBLE(s);
            
        if (x==y) push_LONG(s, 1);
        else push_LONG(s, 0);

    }  else if(has_type(top(s), LONG) && has_type(penultimo(s), CHAR)){
        long x = pop_LONG(s);
        char y = pop_CHAR(s);
            
        if (x==y) push_LONG(s, 1);
        else push_LONG(s, 0);

    }  else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), CHAR)){
        double x = pop_DOUBLE(s);
        char y = pop_CHAR(s);
            
        if (x==y) push_LONG(s, 1);
        else push_LONG(s, 0);
    } else if(  has_type(top(s), LONG) && has_type(penultimo(s), arrays)    ){
           long n = pop_LONG(s);
           struct stack* array = pop_arrays(s);

           push(s, array->stack[n]);

    } else if(  has_type(top(s), CHAR) && has_type(penultimo(s), arrays)    ){
           char n = pop_CHAR(s);
           struct stack* array = pop_arrays(s);

           push(s, enesimo(array, (long)n));
    } else if(has_type(top(s), LONG) && has_type(penultimo(s), STRING)){
        long x = pop_LONG(s);
        char *string = pop_STRING(s);

        push_CHAR(s, string[x]);

    } else if(has_type(top(s), STRING) && has_type(penultimo(s), STRING)){
        char* s1 = pop_STRING(s);
        char* s2 = pop_STRING(s);

        if(strcmp(s1,s2) == 0) push_LONG(s, 1);
        else push_LONG(s, 0);
    

    }

}



/**
* @param s Passagem da stack como parametro
*/
void menor(STACK *s){
    if(has_type(top(s), LONG) && has_type(penultimo(s), LONG)){
        long x = pop_LONG(s);
        long y = pop_LONG(s);
            
        if (x >= y) push_LONG(s, 1);
        else push_LONG(s, 0);


    } else if(has_type(top(s), LONG) && has_type(penultimo(s), DOUBLE)){
        long x = pop_LONG(s);
        double y = pop_DOUBLE(s);
            
        if (x >= y) push_LONG(s, 1);
        else push_LONG(s, 0);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), LONG)){
        double x = pop_DOUBLE(s);
        long y = pop_LONG(s);
            
        if (x>=y) push_LONG(s, 1);
        else push_LONG(s, 0);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), DOUBLE)){
        double x = pop_DOUBLE(s);
        double y = pop_DOUBLE(s);
            
        if (x>=y) push_LONG(s, 1);
        else push_LONG(s, 0);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), CHAR)){
        char x = pop_CHAR(s);
        char y = pop_CHAR(s);
            
        if (x>=y) push_LONG(s, 1);
        else push_LONG(s, 0);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), LONG)){
        char x = pop_CHAR(s);
        long y = pop_LONG(s);
            
        if (x>=y) push_CHAR(s, 1);
        else push_LONG(s, 0);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), DOUBLE)){
        char x = pop_CHAR(s);
        double y = pop_DOUBLE(s);
            
        if (x>=y) push_LONG(s, 1);
        else push_LONG(s, 0);

    }  else if(has_type(top(s), LONG) && has_type(penultimo(s), CHAR)){
        long x = pop_LONG(s);
        char y = pop_CHAR(s);
            
        if (x>=y) push_LONG(s, 1);
        else push_LONG(s, 0);

    }  else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), CHAR)){
        double x = pop_DOUBLE(s);
        char y = pop_CHAR(s);
            
        if (x>=y) push_LONG(s, 1);
        else push_LONG(s, 0);
    
    }  else if(has_type(top(s), LONG) && has_type(penultimo(s), STRING)){
        long x = pop_LONG(s);
        char* string = pop_STRING(s);

        char *string2 = malloc(sizeof(char)*x);

        push_STRING(s, memcpy(string2, string, x));
    }  else if(has_type(top(s), STRING) && has_type(penultimo(s), STRING)){
        char* s1 = pop_STRING(s);
        char* s2 = pop_STRING(s);

        push_LONG(s, strcmp(s2, s1)<0);
        
    }

}

/**
* @param s Passagem da stack como parametro
*/
void maior(STACK *s){
    if(has_type(top(s), LONG) && has_type(penultimo(s), LONG)){
        long x = pop_LONG(s);
        long y = pop_LONG(s);
            
        if (x < y) push_LONG(s, 1);
        else push_LONG(s, 0);


    } else if(has_type(top(s), LONG) && has_type(penultimo(s), DOUBLE)){
        long x = pop_LONG(s);
        double y = pop_DOUBLE(s);
            
        if (x < y) push_LONG(s, 1);
        else push_LONG(s, 0);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), LONG)){
        double x = pop_DOUBLE(s);
        long y = pop_LONG(s);
            
        if (x<y) push_LONG(s, 1);
        else push_LONG(s, 0);

    } else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), DOUBLE)){
        double x = pop_DOUBLE(s);
        double y = pop_DOUBLE(s);
            
        if (x<y) push_LONG(s, 1);
        else push_LONG(s, 0);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), CHAR)){
        char x = pop_CHAR(s);
        char y = pop_CHAR(s);
            
        if (x<y) push_LONG(s, 1);
        else push_LONG(s, 0);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), LONG)){
        char x = pop_CHAR(s);
        long y = pop_LONG(s);
            
        if (x<y) push_CHAR(s, 1);
        else push_LONG(s, 0);

    } else if(has_type(top(s), CHAR) && has_type(penultimo(s), DOUBLE)){
        char x = pop_CHAR(s);
        double y = pop_DOUBLE(s);
            
        if (x<y) push_LONG(s, 1);
        else push_LONG(s, 0);

    }  else if(has_type(top(s), LONG) && has_type(penultimo(s), CHAR)){
        long x = pop_LONG(s);
        char y = pop_CHAR(s);
            
        if (x<y) push_LONG(s, 1);
        else push_LONG(s, 0);

    }  else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), CHAR)){
        double x = pop_DOUBLE(s);
        char y = pop_CHAR(s);
            
        if (x<y) push_LONG(s, 1);
        else push_LONG(s, 0);
    
    }   else if(has_type(top(s), LONG) && has_type(penultimo(s), STRING)){
        long x = pop_LONG(s);
        char* string = pop_STRING(s);
        int i = 0;
        

        char* r = calloc(1, sizeof(char)* (x+1));

        while(x != 0){
            r[i] = string[strlen(string) - x];
            i++;
            x--; 
        }

        push_STRING(s, r);
    } else if(has_type(top(s), STRING) && has_type(penultimo(s), STRING)){
        char* s1 = pop_STRING(s);
        char* s2 = pop_STRING(s);

        push_LONG(s, strcmp(s2, s1)>0);
        
    }


}


/**
* @param s Passagem da stack como parametro
*/
void nao(STACK *s){
    if(has_type(top(s), LONG)){
      long x = pop_LONG(s);
      if(x != 0) push_LONG(s, 0);
      else push_LONG(s,1);
    }


    if(has_type(top(s), DOUBLE)){
      double x = pop_DOUBLE(s);
      if(x != 0) push_LONG(s, 0);
      else push_LONG(s,1);
    }

    if(has_type(top(s), CHAR)){
        char x = pop_CHAR(s);
        if(x != 0) push_LONG(s, 0);
        else push_LONG(s,1);
    }
    
}


/**
* @param s Passagem da stack como parametro
*/
void ifthenelse(STACK *s){   // 1 2 3 ? = 2
    DATA x = pop(s);    // 2 
    DATA y = pop(s);    // 3
    

    if(has_type(top(s), LONG)){
        long z = pop_LONG(s);
        if (z == 0) push(s, x);
        else push(s, y);
    } else if(has_type(top(s), DOUBLE)){
        double z = pop_DOUBLE(s);
        if (z == 0) push(s, x);
        else push(s, y);
    } else if(has_type(top(s), CHAR)){
        char z = pop_CHAR(s);
        if (z == 0) push(s, x);
        else push(s, y);

    } else if(has_type(top(s), arrays)){
        struct stack* array = pop_arrays(s);
        if(array->n_elems == 0) push(s,x);
        else push (s,y);
    }
      
}


/**
* @param s Passagem da stack como parametro
*/
void ee(STACK *s){
    if(has_type(top(s), LONG) && has_type(penultimo(s), LONG)){
        long x = pop_LONG(s);       // x long
        long y = pop_LONG(s);       // y long

        if((x != 0) && (y != 0))
            push_LONG(s, x);
        else push_LONG(s, 0);
    }
    else if(has_type(top(s), LONG) && has_type(penultimo(s), DOUBLE)){
        long x = pop_LONG(s);       // x long
        double y = pop_DOUBLE(s);       // y long

        if((x != 0) && (y != 0))
            push_DOUBLE(s, x);
        else push_LONG(s, 0);
    }
    else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), LONG)){
        double x = pop_DOUBLE(s);       // x long
        long y = pop_LONG(s);       // y long

        if((x != 0) && (y != 0))
            push_LONG(s, x);
        else push_LONG(s, 0);
    }
    else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), DOUBLE)){
        double x = pop_DOUBLE(s);       // x long
        double y = pop_DOUBLE(s);       // y long

        if((x != 0) && (y != 0))
            push_DOUBLE(s, x);
        else push_LONG(s, 0);
    }
    else if(has_type(top(s), CHAR) && has_type(penultimo(s), CHAR)){
        char x = pop_CHAR(s);       // x long
        char y = pop_CHAR(s);       // y long

        if((x != 0) && (y != 0))
            push_CHAR(s, x);
        else push_LONG(s, 0);
    }
    else if(has_type(top(s), LONG) && has_type(penultimo(s), CHAR)){
        long x = pop_LONG(s);       // x long
        char y = pop_CHAR(s);       // y long

        if((x != 0) && (y != 0))
            push_CHAR(s, x);
        else push_LONG(s, 0);
    }
    else if(has_type(top(s), CHAR) && has_type(penultimo(s), LONG)){
        char x = pop_CHAR(s);       // x long
        long y = pop_LONG(s);       // y long

        if((x != 0) && (y != 0))
            push_LONG(s, x);
        else push_LONG(s, 0);
    }
    else if(has_type(top(s), CHAR) && has_type(penultimo(s), DOUBLE)){
        char x = pop_CHAR(s);       // x long
        double y = pop_DOUBLE(s);       // y long

        if((x != 0) && (y != 0))
            push_DOUBLE(s, x);
        else push_LONG(s, 0);
    }
    else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), CHAR)){
        double x = pop_DOUBLE(s);       // x long
        char y = pop_CHAR(s);       // y long

        if((x != 0) && (y != 0))
            push_CHAR(s, x);
        else push_LONG(s, 0);
    }


}


/**
* @param s Passagem da stack como parametro
*/
void eou(STACK *s){
    if(has_type(top(s), LONG) && has_type(penultimo(s), LONG)){
        long x = pop_LONG(s);       // x long
        long y = pop_LONG(s);       // y long

        if(y != 0)
            push_LONG(s, y);
        else push_LONG(s, x);
    }
    else if(has_type(top(s), LONG) && has_type(penultimo(s), DOUBLE)){
        long x = pop_LONG(s);       // x long
        double y = pop_DOUBLE(s);       // y long

        if(y != 0)
            push_DOUBLE(s, y);
        else push_LONG(s, x);
    }
    else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), LONG)){
        double x = pop_DOUBLE(s);       // x long
        long y = pop_LONG(s);       // y long

        if(y != 0)
            push_LONG(s, y);
        else push_DOUBLE(s, x);
    }
    else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), DOUBLE)){
        double x = pop_DOUBLE(s);       // x long
        double y = pop_DOUBLE(s);       // y long

        if(y != 0)
            push_DOUBLE(s, y);
        else push_DOUBLE(s, x);
    }
    else if(has_type(top(s), CHAR) && has_type(penultimo(s), CHAR)){
        char x = pop_CHAR(s);       // x long
        char y = pop_CHAR(s);       // y long

        if(y != 0)
            push_CHAR(s, y);
        else push_CHAR(s, x);
    }
    else if(has_type(top(s), LONG) && has_type(penultimo(s), CHAR)){
        long x = pop_LONG(s);       // x long
        char y = pop_CHAR(s);       // y long

        if(y != 0)
            push_CHAR(s, y);
        else push_LONG(s, x);
    }
    else if(has_type(top(s), CHAR) && has_type(penultimo(s), LONG)){
        char x = pop_CHAR(s);       // x long
        long y = pop_LONG(s);       // y long

        if(y != 0)
            push_LONG(s, y);
        else push_CHAR(s, x);
    }
    else if(has_type(top(s), CHAR) && has_type(penultimo(s), DOUBLE)){
        char x = pop_CHAR(s);       // x long
        double y = pop_DOUBLE(s);       // y long

        if(y != 0)
            push_DOUBLE(s, y);
        else push_CHAR(s, x);
    }
    else if(has_type(top(s), DOUBLE) && has_type(penultimo(s), CHAR)){
        double x = pop_DOUBLE(s);       // x long
        char y = pop_CHAR(s);       // y long

        if(y != 0)
            push_CHAR(s, y);
        else push_DOUBLE(s, x);
    }


}
