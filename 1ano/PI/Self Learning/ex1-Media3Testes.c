#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main() {
    setlocale(LC_ALL, "");

    // declarando variáveis
    float nota1, nota2, nota3, media;

    // obtendo as 3 notas
    printf("Digite a nota 1\n");
    scanf("%f", &nota1);

    printf("Digite a nota 2\n");
    scanf("%f", &nota2);

    printf("Digite a nota 3\n");
    scanf("%f", &nota3);

    // fazendo a média
    media = (nota1 + nota2 + nota3) / 3 ; 

    // condição que me dá o resultado, se media > 7 aprovado , senão reprovado.
    if (media > 7 ) {
        printf("Parabens foi aprovado com media de %.2f\n", media);
    } else {
        printf("Vemo-nos no proximo ano, esta reprovado com media de %.2f\n", media);
    }

    system("pause");
}