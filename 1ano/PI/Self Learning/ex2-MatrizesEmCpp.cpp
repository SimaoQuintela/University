#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>

using namespace std;

// preencher uma matriz 2x2 lendo valores do utilizador e trocar a 1 com a 2 linha

int main() {
    // declrando variáveis 
    int matriz[2][2], i, j;

    // pedindo ao utilizador para inserir os numeros da matriz
    cout << "Insira os numeros da matriz\n";

    for(i=1; i>=0  ; i--) {
        for(j=0 ; j<2 ; j++){
            cin >> matriz[i][j];
        }
    }

    for(i=0; i<2; i++) {
        for( j=0; j<2; j++) {
            cout << matriz[i][j] << " ";
        }
        cout << "\n";
    }
    system("pause");
}