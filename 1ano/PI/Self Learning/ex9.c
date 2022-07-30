#include <stdio.h>
#include <stdlib.h>

/* dados dois numeros inteiros positivos i e j , diferentes de 0. Imprimir
em ordem crescente os n primeiros naturais que são multiplos de i ou de j*/

void main() {

    // declarando variáveis
    int n, i, j, acc, numero; // acc means accumulator

    // pedindo os dados ao utilizador
    printf("Insira o valor para n: ");
    scanf("%d", &n);

    printf("Insira o valor para i: ");
    scanf("%d", &i);

    printf("Insira o valor para j: ");
    scanf("%d", &j);

    numero = 1; // Representa o número que estamos a dividir
    acc = 0;    // Representa a quantidade de números selecionados

    while(acc < n) {
        /* Se o numero for divisivel por i ou por j fica-se com ele
        e portanto aumenta-se 1 ao acumulador e salta-se para o proximo numero*/
        if (numero % i == 0 || numero % j == 0) {
            printf("%d ", numero);
            acc++;
            numero++;
        } else {      // caso não seja divisível salta-se para o próximo numero
            numero++;
        }    
    }
    printf("\n");
    system("pause");
}