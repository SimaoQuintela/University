#include <stdio.h>
#include <stdlib.h>


void main() {

    int numero, quadrado;

    printf("Insira um numero, quando quiser acabar a sequência introduza o numero 0\n"); // pedir ao utilizador um número
    scanf("%d",&numero);  // utilizador introduz um número

    while(numero != 0) {
        quadrado = numero * numero;
        printf("O quadrado de %d e %d\n", numero, quadrado);
        scanf("%d", &numero);
    }

    system("pause");
}