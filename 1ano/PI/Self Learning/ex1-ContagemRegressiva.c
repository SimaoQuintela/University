#include <stdio.h>
#include <stdlib.h>

// Criar um algoritmo que imprima os numeros de 0 até 10 de forma regressiva
// Usando while , do while e for


#define ZERO 0

void main() {

    // declarando variáveis
    int i = 10, opcao;

    // caso o utilizador introduza uma opcao invalida, dá-lhe tentativas infinitas até acertar 
    while (opcao < 1 || opcao > 3) {
    // interface de selecao
    printf("Escolha o metodo que quer usar para a contagem regressiva de 10 ate 0\n");
    printf("1 - while\n");
    printf("2 - do while\n");
    printf("3 - for\n");
    // para o utilizador escolher a opcao
    scanf("%d", &opcao);
    printf("\n");

    switch (opcao){
    // utilizando o while 
        case 1: while (i >= ZERO) {
                    printf("%d\n", i);
                    i--;
                }
            break;

    // utilizando o do while        
        case 2:  i = 10;
                 do {
                    printf("%d\n", i);
                    i--;
                    } while (i >= ZERO);
            break;
        
    // utilizando o for
        case 3: for (i = 10; i >= ZERO; i--) {
                     printf("%d\n", i);
                     }
            break;

        default: printf("Opcao invalida. Tente de novo\n");
            break;    }
    }
    system("pause");

    }