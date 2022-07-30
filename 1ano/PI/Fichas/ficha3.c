#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//1 a 
int ex1a(){
    
    int x [15] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};

    int *y, *z, i;
    y = x; z = x + 3;     // y = endereço de x que corresponde à posicao 0, logo y = 1
                          // z = endereço de x + 3 logo corresponde à posicao 3, logo z = 4
    for(i=0; i<5; i++){
        printf("%d %d %d\n", x[i], *y, *z);
        y = y+1; z = z+2;
    }
    // para i = 0 -   1 1 4
    // para i = 1 -   2 2 6
    // para i = 2 -   3 3 8
    // para i = 3 -   4 4 10
    // para i = 4 -   5 5 12
    return 0 ;
}

//1 b 

int ex1b(){
    int i, j, *a, *b;

    i = 3;
    j = 5;

    a = &i;  // 3
    b = &j;  // 5

    i++;   // i = 4

    j = i + *b;  //  j = 4 + 5 = 9
    b = a;       // b = 4  
    j = j + *b;  // j = 9 + 4

    printf("%d\n", j); //   13 

    return 0;
}

//2
void swapM(int *x, int *y){
    int temp;

    temp = *x;
    *x = *y;
    *y = temp;
}

//3
 swap(int v[], int i, int j){
    int temp;
    
    temp = v[i];
    v[i] = v[j];
    v[j] = temp;
}

//4
int soma (int v[], int N){
    int soma = 0, i = 0;

    while(N != 0){
        soma += v[i];
        i++;
        N--;
    }

    return soma;
}

//5 primeira versão
void inverteArray1 (int v[], int N){
    int i;

    if(N % 2 == 0){
        for(i=0; i<(N/2); i++)
            swap(v, i, N-i-1);
    } else {
        for(i=0; i<=(N/2); i++)
            swap(v, i, N-i-1);
    }

    for(i=0; i<N; i++) 
        printf("%d ", v[i]);
}


// segunda versão 
void inverteArray2 (int v[], int N){
    int i;
    int newArray[N];

    for(i=0; i<N; i++){
        newArray[i] = v[N-1-i];
    }

    for(i=0; i<N; i++)
        printf("%d ", newArray[i]);
}

//6
int maximum(int v[], int N, int *m){
    int i;

    *m = v[0];

    if(N <= 0){
        return 1;
    } else {
        for(i=1 ; i < N; i++){
            if(v[i] > *m)
                *m = v[i];
        }
        return 0;
    }
}

//7
void quadrados (int q[], int N){
    int quadrado = 1, i;

    for(i=0; i<N ; i++){
        q[i] = quadrado*quadrado;
        quadrado++;
    }
    return 0;
}

//8 




int main() {
  int v[10]={0};
  int array[10] = {1,2,3,4,5,6,7,8,9,10};

  quadrados(v, 10); 
  
  inverteArray1(array, 10);
  inverteArray2(array, 10);
  
  return 0;
}






