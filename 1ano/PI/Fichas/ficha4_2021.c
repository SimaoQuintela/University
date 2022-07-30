#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//1- Funções sobre Strings 
//1.
int eVogal(char c){
	int k;
	int resultado;
	char vogais[11] = "aAeEiIoOuU";

	k=0;
	while(vogais[k]){
		if(vogais[k] == c){
			resultado = 1;
			break;
		}
		k++;
	}
	return resultado;
}

int contaVogais(char *s){
	int i= 0;
	int count = 0;

	while(s[i]){
		if(eVogal(s[i]))
			count++;
		i++;
	}
	return count;
}

//2. com array auxiliar 
int retiraVogaisRep(char *s){
	int count=0, i=0, j=0;
	char aux[strlen(s)];
	int anterior=0, resultado=0;

	while(s[i]){
		if(anterior!=0 && anterior == s[i])
			resultado++;
		else {
			aux[j] = aux[i];
			j++;
			if(eVogal(s[i]))
				anterior = s[i];
			else 
				anterior = 0;
		}
		i++;
	}
	aux[j] = '\0';

	for(;j>=0; j--)
		s[j] = aux[j];

	return resultado;

}
//2. sem o array auxiliar
int retiraVogaisRep2(char *s){
	int i=0,j=0, resultado=0, anterior=0;

	while(s[i]){
		if(anterior!=0 && anterior == s[i]){
			resultado++;
			for(j=i; s[j]; j++)
				s[j] = s[j+1];
		}else {
			if(eVogal(s[i]))
				anterior = s[i];
			else 
				anterior = 0;
			i++;
		}
	}

	return resultado;
}

//3. com array auxiliar
int duplicaVogais(char *s){
	char aux[strlen(s) + contaVogais(s)];
	int i=0,j=0, resultado=0;

	while(s[i]){
		if(eVogal(s[i])){
			s[j] = s[i];
			j++;
			s[j] = s[i];
			j++;
			resultado++;
		} else {
			s[j] = s[i];
			j++;
		}
		i++;
	}
	for(i=0; s[i]; i++)
		s[i] = aux[i];

	return resultado;
}

//2- Arrays ordenados 
//1.
int ordenado(int v[], int N){
	int i=0, resultado;

	while(v[i] && v[i] <= v[i+1])
		i++;


	if(i==N)
		resultado = 1;
	else
		resultado = 0;


	return resultado;
}

//2.
void merge (int r [], int a[], int b[], int na, int nb){
    int i=0, j=0, k;

    for(k=0; i<na && j<nb; k++){
        if(a[i] < b[j]){
            r[k] = a[i];
            i++;
        } else {
            r[k] = b[j];
            j++;
        }
    }
            
    while(i<na){
        r[k] = a[i];
        k++;
        i++;
    }

    while(j<nb){
        r[k] = b[j];
        k++;
        j++;
    }
}

//3. com array auxiliar
int partition(int v[], int N, int x){
	int array[N];
	int i = 0, j = N-1;
	int k;

	for(k = 0; v[k]; k++){
		if(v[k] <= x){
			array[i] = v[k];
			i++;
		} else {
			array[j] = v[k];
			j--;
		}
	}

	while(k>=0){
		v[k] = array[k];
		k++;
	}
	return i;
}

// sem array auxiliar
void swap(int v[], int i, int j){
	int temp;

	temp = v[i];
	v[i] = v[j];
	v[j] = temp;
}

int partition2(int v[], int N, int x){
	int i= -1, j=0;

	while(v[j]){
		if(v[j]>x)
			j++;
		else {
			i++;
			swap(v,i,j);
			j++;
		}
	}

	j-=2;
	while(x < v[j]){
		swap(v,x,j);
		j--;
	}

	return i+1;
}

