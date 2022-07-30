#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define Size 10

typedef struct nodo
{
	char *chave;
	int ocorr;
	struct nodo *prox;
} Nodo, *THash[Size];

unsigned hash(char *str)
{
	unsigned hash = 5381;
	int c;
	while (c = *str++)
		hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
	return hash;
}

void add(char *s, THash t)
{
	int pos = hash(s) % Size;
	Nodo *aux, *anterior;
	Nodo *novo = malloc(sizeof(Nodo));
	novo->prox = NULL;
	novo->chave = strdup(s);
	novo->ocorr = 1;

	if (t[pos] != NULL)
	{
		for (aux = t[pos]; aux != NULL && strcmp(aux->chave, s); aux = aux->prox)
			anterior = aux;

		if (aux == NULL)
		{
			anterior->prox = novo;
		}
		else
			aux->ocorr += 1;
	}
	else
		t[pos] = novo;
}

void printHashTable(THash t)
{
	int i = 0;
	Nodo *aux;

	for (i = 0; i < Size; i += 1)
	{
		aux = t[i];
		printf("Nivel %d ---> ", i);
		while (aux != NULL)
		{
			printf(aux->chave);
			printf(" ->");
			aux = aux->prox;
		}
		printf("\n");
	}
}

int main()
{
	int i;
	THash t;

	for (i = 0; i < Size; i++)
		t[i] = NULL;

	add("simao", t);
	add("simao", t);
	add("naruto", t);
	add("ross", t);
	add("rachel", t);
	add("monica", t);
	add("phoebe", t);
	add("chandler", t);
	add("joey", t);
	add("nuno", t);
	add("guedes", t);

	printHashTable(t);
	getchar();
}
