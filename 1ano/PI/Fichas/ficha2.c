#include <stdio.h>
#include <stdlib.h>

//1

float multInt (int n, float m){
    // declarando variáveis
    int r, i;
    r = 0;
    
    for (i=0; i<n; i++){
        r = r + m;
    }

    return r;
}

// 2
float multInt2 (int n, float m){
    float resultado = 0;

    while(n>=1){
        if(n % 2 != 0){
            resultado = resultado + m;
            n = n / 2;
            m = m * 2;
        } else {
            n = n / 2;
            m = m * 2;
        }
    }

    return resultado;
}
/* para testar o resultado
float main(){
    printf("%.0f", multInt2(81,423));
    return 0;
}
*/

//3
// esta definição está super longa porém faz menos passagens pela função do que a definição alternativa abaixo

int mdc (int a, int b){
    // declarando variáveis
    int i = 2;
    int divisor = 2; // tenho de corrigir isto , começa em 1

    if (a<b){
        while((a/i)!=1){
            if ((a % i) == 0){
                a = a / i;
                if ((i >= divisor) && (b % i == 0))
                    divisor = i;
            } else {
                i++;
            }
        }
    } else {
        while((b/i)!=1){
            if ((b % i) == 0){
                b = b / i;
                if ((i >= divisor) && (a % i == 0)) 
                    divisor = i;
            } else {
                i++;
            }
        }
    }
    return divisor;
}

// definição alternativa e mais simplificada mas menos eficiente pois faz muitas mais passagens pela função 

int mdc2 (int a, int b){
    // declaração de variáveis
    int i, divisor;

    if (a<b){
        for(i=0; i<=a; i++){
            if (a % i == 0 && b % i == 0)
            divisor = i;
        }
    } else {
        for(i=0; i<=b; i++){
            if (b % i == 0 && a % i == 0)
            divisor = i;
        }
    }
    return divisor;
}  

//4
int mdcAlternativo (int a, int b){

    while(a>0 && b>0){
        if(a>b){
            a = a-b;
        } else {
            b = b-a;
        }
    }
    // sabemos que a condiçao (a>0) && (b>0) é falsa
    // logo, (a<=0) || (b<=0) é
    if (a>0) return a;
    else return b;
}

int mdc3 (int a, int b, int *count){
    (*count) = 0;
    while(a>0 && b>0){
        if(a>b){
            a = a-b;
        } else {
            b = b-a;
        }
        *count = += 1; // incrementar o contador
    }

    if (a>0) return a;
    else return b;

    // ainda devolve o numero de iterações através de (*count)
}




//5
int mdc4 (int a, int b, int *count){
    (*count) = 0;
    
    while(a!=0 && b!= 0){
        if(a>b){
            a = a %b;
        } else {
            b = b%a;
        }
    (*count) += 1;
    }
    
    if(a>0) return a; 
    else return b;

}

//6 
//a

int fib(int n){
    int r;

    if(n<=2) // condição de paragem 
        r=1;
    else     // passo recursivo
        r = fib(n-1) + fib(n-2);




}


//b
int fib2 (int n){
    int i, resultado;
    int a = 1;
    int b = 1;

    if (n==1 || n == 0){
        return 1;
    }
    for(i=1; i < n; i++){
        resultado = a + b;
        a = b;
        b = resultado;
    }

    return resultado;
}

int main(){
    printf("%d", fib2(15));
    return 0;
}