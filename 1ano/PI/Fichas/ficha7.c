typedef struct celula {
	char *palavra;
	int ocorr;
	struct celula * prox;
} * Palavras;

// criar uma célula
Palavras novaCelula(char *p, int ocorr){
	Palavras nova = malloc(sizeof(struct celula));
	nova->prox = NULL;
	nova->palavra = strdup(p);
	nova->ocorr = ocorr;

	return nova;
} 


//1.
void libertaLista (Palavras l){
	if(l != NULL){
		libertaLista(l->prox);
		free(l);
	}
}

//2.
int quantasP(Palavras l){
	int words = 0;

	while(l != NULL){
		words++;
		l = l->prox;
	}

	return words;
}

//3.
void listaPal (Palavras l){

	while(l != NULL){
		printf("%s numero de ocorrencias: %d", l->palavra, l->ocorr);
		l = l->prox;
	}
}

//4.
char *ultima (Palavras l){

	while(l->prox != NULL) l = l->prox;
	
	return l->palavra;
}

//5.
Palavras acrescentaInicio (Palavras l, char *p){
	Palavras nova = novaCelula(p, 1);

	nova->prox = l;

	return nova;
}

//6.
Palavras acrescentaFim (Palavras l, char *p){
	Palavras move = l; 
	Palavras nova = novaCelula(p,1);

	if(l == NULL)
		l = nova;
	else {
		while(move->prox != NULL)
			move = move->prox;
		
		move->prox = nova;
	}

	
	return l;
}

//7. está incompleto
Palavras acrescenta(Palavras l, char *p){
	Palavras nova = novaCelula(p, 1);
	Palavras move = l;
	Palavras anterior = l;
	
	if(l == NULL)
		l = nova;
	else {
		while(move->prox != NULL && strcmp(p, move->palavra) < 0){
			anterior = move;
			move = move->prox;
		}

		if (strcmp(p, move->palavra) == 0)
			move->ocorr++;
		else if(move->prox == NULL){
			move->prox = nova;
		} else {
			nova->prox = move;
			anterior->prox = nova;
		}

	}

	return l;
}


//8. 
struct celula * maisFreq (Palavras l) {
    int max = 0;
    Palavras mais_freq = malloc(sizeof(struct celula));
    for (; l != NULL; l = l->prox) {
        if (l->ocorr > max) {
            max = l->ocorr;
            mais_freq = l;
        }
    }
    return mais_freq;
}