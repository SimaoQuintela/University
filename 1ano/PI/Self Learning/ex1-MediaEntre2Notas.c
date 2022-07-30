#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main (){
    setlocale(LC_ALL,"");

    // exercício nº 1, um programa que lê 2 notas e faz a sua média 
    
    // declaração de dados
    float nota1, nota2, media; 
    
    // nota do 1 teste
    printf("Insira a primeira nota:");
    scanf("%f", &nota1);

    // nota do 2 teste 
    printf("Insira a segunda nota:");
    scanf("%f", &nota2);
    
    // média dos 2 testes
    media = ((nota1 + nota2) / 2);
    printf("A média dos 2 testes e %f", media);
}