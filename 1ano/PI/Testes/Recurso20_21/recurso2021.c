#include <stdio.h>
#include <stdlib.h>

//ex1.
void swap(int v[], int indice1, int indice2){
	
	int temp = v[indice1];
	v[indice1] = v[indice2];
	v[indice2] = temp;
}

int conta_pares(int v[], int N){
	int i, pares = 0;

	for(i=0; i<N; i++)
		if(v[i] % 2 == 0)
			pares++;
		else
			break;

	return pares;
}

int paresImpares(int v[], int N){
	int i, j;

	// coloca primeiro os pares e depois os impares
	for(i=0; i<N; i++)
		for(j=i; j<N; j++){
			if(v[i] % 2 == 1 && v[j] % 2 == 0){	
				swap(v, i, j);
				break;	//eficiencia (y)
			}
		}

	int pares = conta_pares(v, N);

	//testando
	for(i=0; i<N; i++)
		printf("%d ", v[i]);

	printf("\n%d", pares);
	//

	return pares;
}

//ex2.
void merge(LInt *r, LInt a, LInt b){

	while(a || b){
		if( (a && b && a->valor < b->valor) || b == NULL ){
			*r = a;
			a = a->prox;
			r = &(*r)->prox;
		} else {
			*r = b;
			b = b->prox;
			r = &(*r)->prox; 
		}
	}


	*r = NULL;
}

//ex3.
void latino(int N, int m[N][N]){
	int i, j;

	for(i=0; i<N; i++){
		for(j=0; j<N; j++){
			if(i+j<N){
				m[i][j] = i+j+1;
	// 			printf("%d ", m[i][j]);
			}
			else{
				m[i][j] = i+j-N+1;
	//  		printf("%d ", m[i][j]);
			}
		}
	//	printf("\n");
	}
}

typedef struct nodo{
	int valor;
	struct nodo *pai, *esq, *dir;
} *ABin;


//ex.4   (não entendi bem o enunciado mas penso que seja isto)
ABin next(ABin a){
	if(!a)
		return NULL;

	else if(a->esq && a->dir){
		while(a->esq)
			a = a->esq;
		return a;
	
	} else if(!(a->esq))
		return a;

	else {
		while(a->dir)
			a = a->dir;
		return a;
	}
}











int main(){
	// testing
	int array[10] = {2 , 6, 4, 1, 3, 8, 10, 5, 7, 9};
	//paresImpares(array, 10);

	//ex.3
	int matriz[3][3];
	latino(2, matriz);

	return 0;
}