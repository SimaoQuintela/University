#include <stdio.h>
#include <stdlib.h>

void main() {

    // declarando variáveis
    float a, b, soma, subtracao, divisao, multiplicacao;
    int operacao;

    // Deixar o utilizador escolher os 2 números
    printf("Escolha 2 numeros\n");
    scanf("%f %f", &a, &b);

    // Escolher a operação que quer realizar 
    printf("Escolha a operacao a realizar entre esses 2 numeros\n");
    printf("1-Soma\n");
    printf("2-Subtracao\n");
    printf("3-Divisao\n");
    printf("4-Multiplicacao\n");
    
    scanf("%d", &operacao);
    
    soma = a + b;
    subtracao = a - b;
    multiplicacao = a * b;
    divisao = a / b; 

    switch(operacao) {
            case 1: printf("A soma de a com b da %.2f\n", soma);
                break;
            
            case 2: printf("A subtracao de a com b da %.2f\n", subtracao);
                break;
            
            case 3: printf("A divisao de a por b da %.2f\n", divisao);
                break;
            
            case 4: printf("A multiplicacao de a por b da %.2f\n", multiplicacao);
                break;
            
            default: printf("Operacao invalida\n");
                break;
        }

    system ("pause");

}