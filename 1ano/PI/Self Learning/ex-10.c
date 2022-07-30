#include <stdio.h>
#include <stdlib.h>

    // verificar se um número é triangular, exemplo: 120 é triangular porque 4 x 5 x 6 = 120

void main() {

    // declarando variáveis
    int numero, a, b, c; // a b c são 3 números consecutivos

    printf("Insira um numero a sua escolha: ");
    scanf("%d", &numero);

    a = 1;
    b = 2;
    c = 3;

    while (a * b * c <= numero) {
        if (a * b * c == numero) {
            printf("O numero %d e' triangular pois %d x %d x %d = %d\n", numero, a, b, c, numero);
            a++;
            b++;
            c++;
        } else {
            a++;
            b++;
            c++;
        }
    }
    a--;
    b--;
    c--;

    if ( a * b * c < numero) {
        printf("O numero %d nao e' triangular\n", numero);
    }

    system("pause");
}
