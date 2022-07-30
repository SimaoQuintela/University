#include <stdio.h>
#include <stdlib.h>

/* ler 3 valores de um vetor e fazer a média desses 3 valores */
/*
void main() {

    // declarar variáveis
    float vetor[3], media;
    // Obtendo o valor dos 3 vetores    
    printf("Insira o valor dos 3 vetores\n");
    
    printf("Vetor 1: ");
    scanf("%f", &vetor[0]);

    printf("\nVetor 2: ");
    scanf("%f", &vetor[1]);

    printf("\nVetor 3: ");
    scanf("%f", &vetor[2]);

    // valor da média
    media = (vetor[0] + vetor[1] + vetor[2]) / 3 ; 
    // resultado final
    printf("\nA media dos 3 vetores e %.2f \n", media);

    system("pause");
}

*/



// Usando for 

void main() {

    // declarando variáveis 
    int pos = 0;
    float vetor[3], media;

    for(pos = 0; pos < 3; pos++) {
        printf("Valor do vetor na posicao %d: ", pos);
        scanf("%f", &vetor[pos]);
    }

    media = (vetor[0] + vetor[1] + vetor[2]) / 3;

    printf("A media do vetor e %.2f\n", media);

    system("pause");
}