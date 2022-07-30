#include <stdio.h>
#include <stdlib.h>

// imprmir os números pares de 10 a 20 usando while , do while e for

void main(){

    int i = 10; 
    // usando while
    while (i >= 10 && i <= 20) {
        if (i % 2 == 0) {
            printf("%d\n", i);
            i++;
        } else {
            i++;
        }
    }

    // usando do while
    i = 10;
    do {
        if (i % 2 == 0) {
            printf("%d\n", i);
            i++;
        } else {
            i++;
        }
    } while (i >= 10 && i <= 20);

    // usando for 
    for (i=10; i >= 10 && i <= 20; i++) {
        if (i % 2 == 0) {
            printf("%d\n", i);
        }
    }

}