#include <stdio.h>
#include <stdlib.h>

// dado um numero inteiro x e um numero inteiro nao negativo n calcular x^n
void main() {

    // declarar variaveis 
    int acc, x, n, operacao;

    // obtendo o valor de x
    printf("Insira um numero para x: ");
    scanf("%d", &x);
    // obtendo o valor de n
    printf("Insira um numero para n: ");
    scanf("%d", &n);

    operacao = x;
    acc = 1;
    /* este ciclo é sempre executado até ao valor do acc ser igual ao numero de vezes que se tem de multiplicar o numero (n vezes) */
    while (acc < n) {
        operacao = operacao * x;
        acc++;
    }

    // resultado final
    printf("o valor de %d^%d e' %d\n", x, n, operacao);

    system("pause");
}