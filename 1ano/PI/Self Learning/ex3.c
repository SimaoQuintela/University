#include <stdio.h>
#include <stdlib.h>

// imprimir os n primeiros numeros ímpares 

void main() {

    // declarando variáveis
    int i = 1, acc = 0, n;

    // pedindo ao utilizador um número natural 
    printf("Insira um numero natural: ");
    scanf("%d", &n);

    printf("Os %d primeiros numeros impares sao: ", n);
    /* acc representa a quantidade de numeros impares que temos no momento
    por isso, quando a quantidade de numeros impares for igual a n o ciclo é
    interrompido. Quando o resto da divisao de i por 2 é diferente de 0 é porque
    o numero é impar logo acrescenta-se 1 ao acumulador e 1 ao i (que é o numero atual)
    e quando o numero é par apenas se acrescenta 1 ao i para passar para o próximo numero*/
    while (acc!= n) {
        if (i % 2 != 0) {
            printf("%d", i);
            i++;
            acc++;
        } else {
            printf(",");
            i++;
        }
        
    }
    printf("\n");
    system("pause");
}