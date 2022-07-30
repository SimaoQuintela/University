// ficha 4 do ano passado :/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

//1
int minusculas(char s[]){
	int alteracoes = 0, i;

	for(i=0; s[i]!='\0'; i++){
		if( s[i]>= 65 && s[i] <= 90){
			s[i] += 32;
			alteracoes++;
		}
	}
	
	return alteracoes;
}

//2
int contaLinhas(char s[]){
	int lines = 1, i;

	for(i=0; s[i]; i++){
		if(s[i] == '\n')
			lines++;
	} 

	printf("%d", lines);

	return lines;
}

//3
int contaPal(char s[]){
	int i=0, words=0;

	while(s[i]){
		if(isspace(s[i]) && !(isspace(s[i-1]))){
			words++;
			i++;
		}
	i++;
	}

	return words;
}


//4
/*
int procura(char *p, char *ps[], int N){
	int i = 0;

	while(i < N){
		if (strcmp(p, ps[i]) == 0)
			return i;
		i++;
	}

	return i;
}
*/

//5

//6


//7
int zeros(int N, int M, int m [N][M]){
	int cont = 0, i, j;

	for(i=0; i<N; i++){
		for(j=0; j<M; j++){
			if (m[i][j] == 0)
				cont++;
		}
	}

	printf("%d", cont);

	return cont;
}

//8
void identidade (int N, int m[N][N]){
	int i, j;

	for(i=0; i<N; i++){
		for(j=0; j<N; j++){
			if (j==i)
				m[i][j] == 1;
			else 
				m[i][j] == 0;
		}
	}
}

//9
void multV (int N, float t[N][N], float v[N], float r[N]){
	int result = 0, i,j;

	for(i=0; i<N; i++){
		for(j=0; j<N; j++){
			result += t[i][j] * v[j];
			}
		r[i] = result;
		result = 0;
	}
}



int main(){

	return 0;
}
