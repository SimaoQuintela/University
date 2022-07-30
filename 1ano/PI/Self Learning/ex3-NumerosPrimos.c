#include <stdlib.h>
#include <stdio.h>

// Algoritmo que lê um número e diz se é primo 

void main() {

    // declaração de variável
    int acumulador = 0, i, numero;
    // escolha do número 
    printf("Numero escolhido: ");
    scanf("%d", &numero);
    /* verificando se o número é primo ou não usando um acumulador que aumenta 1 de valor a cada vez que a divisao do numero escolhido por cada numero até chegar
    ao proprio numero dá 0*/
    for(i = 1; i <= numero; i++) {
        if (numero % i == 0) {
            acumulador++;
        } else {
            acumulador;
        }
    }
    /* se o acumulador ( número de divisores ) for igual a 2 o número é primo , se o resto da divisao do numero por 2 der 0 o numero e par,
     se o resto do numero por 2 der diferente de 0 o numero e impar */
    if (acumulador == 2) {
        printf("O numero %d e primo\n", numero);
    } else {
        if (numero % 2 == 0) {
            printf("O numero %d e par\n", numero);
        } else {
            printf("O numero %d e impar\n", numero);
        }
    }
    system("pause");

}
