#include <stdio.h>
#include <stdlib.h>

/* dado um numero n positivo calcula a soma dos n primeiros
numeros positivos */

void main() {

    // declaração de variáveis
    int soma = 0 ,i, n;
    // pedindo ao utilizador um numero inteiro positivo 
    printf("Insira um numero inteiro positivo: ");
    scanf("%d", &n);
    
    /* percorremos todos os valores inteiros até chegar a n e à medida
    que vamos percorrendo os números somamo-los */    
    for(i = 1 ; i <= n ; i++) {
        soma = i + soma;
    }

    // resultado obtido da soma dos n primeiros numeros positivos
    printf("A soma dos %d primeiros numeros positivos e' %d\n", n, soma);

    system ("pause");
}