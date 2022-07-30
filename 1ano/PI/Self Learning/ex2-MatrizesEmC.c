#include <stdio.h>
#include <stdlib.h>

// preencher uma matriz 2x2 lendo valores do utilizador e trocar a 1 com a 2 linha
/*
void main(){

    // declarando variáveis
    int matriz[2][2], linhas, colunas;

    // recolhendo os dados necessários para construir a matriz
    for (linhas = 1; linhas >= 0; linhas--) {
        for (colunas = 0; colunas < 2; colunas++) {
            printf("Introduza um valor- ");
            scanf("%d", &matriz[linhas][colunas]);
         }                                                                                
    }

    // imprimindo a matriz
    for (linhas = 0; linhas < 2; linhas++) {
        for(colunas = 0; colunas < 2 ; colunas ++) {
            printf("%d ", matriz[linhas][colunas]);
        } 
        printf("\n");
    }

    system ("pause");
} */


void main() {

    // declarar variáveis
    int matriz[2][2], linhas, colunas, aux1, aux2;

    // dizer ao utilizador para colocar os valores pretendidos
    for (linhas = 0; linhas < 2; linhas++) {
        for (colunas = 0; colunas < 2; colunas++) {
            printf("Escolha o numero para a posicao [%d][%d]: ", linhas, colunas);
            scanf("%d", &matriz[linhas][colunas]);
        }
    }
    
    // funções auxiliares 
    aux1 = matriz[0][0];
    aux2 = matriz[0][1];

    // imprimindo os resultados  
    matriz[0][0] = matriz[1][0]; 
    matriz[0][1] = matriz[1][1]; 
    matriz[1][0] = aux1;
    matriz[1][1] = aux2;

    for (linhas = 0; linhas < 2; linhas++) {
        for(colunas = 0; colunas < 2; colunas++) {
            printf("%d ", matriz[linhas][colunas]);
        }
        printf("\n");
    }       

    system("pause");

}