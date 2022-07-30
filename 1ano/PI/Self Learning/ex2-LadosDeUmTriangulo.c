#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main () {
    setlocale(LC_ALL, "");

    // declarar variáveis 
    int lado1, lado2, lado3;

    //Obtendo os lados do triangulo 
    printf("Insira o comprimento do lado1\n");
    scanf("%f", &lado1);

    printf("Insira o comprimento do lado2\n");
    scanf("%f", &lado2);

    printf("Insira o comprimento do lado3\n");
    scanf("%f", &lado3);

    // verificando se os 3 lados são iguais 
    if ((lado1 == lado2) && (lado1 == lado3)) {
        printf("Esses valores formam um triângulo equilátero\n");
    } else {
        printf("Esses valores não formam um triângulo equilátero");
    }

    system("pause");
}