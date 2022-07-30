#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <math.h>

void main() {
    setlocale(LC_ALL, "");

    //exercício 2 , o valor absoluto da diferença de 2 notas
 
    // declarar variáveis 
    float nota1, nota2, resultado, absoluto;

    // obtendo a nota 1 
    printf("Insira a primeira nota\n");
    scanf("%f", &nota1);

    //obtendo a nota2 
    printf("Insira a segunda nota\n");
    scanf("%f", &nota2);

    // o resultado 
    resultado = nota1 - nota2 ; 
    absoluto = abs (resultado);
    printf("%f", absoluto);

  /// resolver o problema com o abs
}