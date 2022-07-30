#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, "");

    // exercício 3 , pegar em 3 números inteiros de uma só vez e multiplica-los

    //declaração de variáveis
    int number1, number2, number3, multiplica;
    
    // Pedir ao usuário para inserir 3 números
    printf("Insira 3 numeros a sua escolha\n");
    //selecionar os 3 números e inseri-los nas variáveis 1 2 e 3 
    scanf("%d %d %d", &number1, &number2, &number3);
    // realizar a sua multiplicação
    multiplica = number1 * number2 * number3;
    printf("O resultado da multiplicacao dos 3 numeros e : %d", multiplica);   




} 