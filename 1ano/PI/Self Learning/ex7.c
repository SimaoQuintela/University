#include <stdio.h>
#include <stdlib.h>

void main() {
    // declranado variáveis
    int n , acc, numeros, somaPares;
    // Peço ao utilizar a informação de quantos números ele vai usar
    printf("Insira a quantidade n de numeros que vai utilizar: ");
    scanf("%d", &n);

    acc = 0;
    somaPares = 0;
    /* o acc representa o número de números digitados pelo utilizador
    portanto, quando o acumulador for igual a n (que é o numero de 
    números inseridos pelo utilizador, o ciclo é interrompido ficando
    o somaPares com o valor daquele momento */
    while (acc != n) {
        printf("Insira o numero desejado: ");
        scanf ("%d", &numeros);
        if (numeros % 2 == 0) {
        somaPares = somaPares + numeros; 
        }  
        acc++;    
    }
    // imprimindo o resultado
    printf("A soma dos %d primeiros numeros pares da' %d\n", n, somaPares);

    system("pause");
}