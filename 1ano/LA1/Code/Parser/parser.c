/**
* @file parser Módulo que contém o parser, que tem como objetivo separar uma string token a token e envia-la para o tokenizador para interpretar os vários tokens.
* \author Simao Quintela
*/
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "stack.h"
#include "parser.h"
#include "maths.h"
#include "tokenizador.h"
#include "manipulacao_da_stack.h"

/**
* \brief A função parse recebe uma stack e uma linha (vindas da main), percorre essa linha separa em token e envia-os um a um para o tokenizador que os vai interpretar.
* \brief Saindo do ciclo for, a função print_stack imprime a stack.
* @param s Passagem da stack como parametro
* @param letras Passagem das letras como parametro
* @param line Linha a ser lida.
*/
void parse(STACK *s, STACK *letras, char *line) {
    int i;
	  char *token = malloc(sizeof(token)*500);

  	while(*line != '\0'){
  		//parte dedicada às strings					/////////////////////		
  		if(*line == '"'){
  			line++;
  			for(i = 0; *line != '"'; i++){
  				token[i] = *line;
  				line++;
  			}
  			line+=1;
  			token[i] = '\0';

  			char *token2;
  			token2 = strdup(token);
  			tokenizador_strings(s, token2);
  		}											////////////////////

  		if(*line == '\0' || *line == '\n')
			break;

  		// parte dedicada aos arrays  				/////////////////////	
  		if(*line == '['){							
  			line++;						
  			while(isspace(*line))
  				line++;

  			int count = 1;    // quantidade de [
  			for(i = 0; count != 0; i++){

  				if(*line == '[')
  					count++;
  				if(*line == ']')
  					count--;

  				token[i] = *line;
  				line++;
  			}
  			token[i-1] = '\0';	

  			STACK *new = new_stack();
  			new = eval(token, letras, new);
  			push_arrays(s, new);
		}											/////////////////////




		if(*line == '\0' || *line == '\n')
			break;

  		// parte dedicada aos não arrays ou strings	
  		if(!isspace(*line)){
  			for(i=0; !isspace(*line) ; i++){
  				token[i] = *line;
  				line++;
  			}
 			token[i] = '\0';
 			tokenizador(s, letras, token);
 		}
  		while(isspace(*line))
  			line++;

  	}
 	print_stack(s);
}


/**
* \brief A função parse2 está responsável por ler linhas subsequentes à primeira e por interpretar arrays aninhados
* @param s Passagem da stack como parametro
* @param letras Passagem das letras como parametro
* @param line Linha a ser lida.
*/
void parse2(STACK *s, STACK *letras, char *line) {
    int i;
	  char *token = malloc(sizeof(token)*300);

  	while(*line != '\0'){
  		//parte dedicada às strings					/////////////////////		
  		if(*line == '"'){
  			line++;
  			for(i = 0; *line != '"'; i++){
  				token[i] = *line;
  				line++;
  			}
  			line+=1;
  			token[i] = '\0';

  			char *token2;
  			token2 = strdup(token);
  			tokenizador_strings(s, token2);
  		}											////////////////////

  		if(*line == '\0' || *line == '\n')
			break;

  		// parte dedicada aos arrays  				/////////////////////	[ 2 3 4 ]
  		if(*line == '['){							
  			line++;						
  			while(isspace(*line))
  				line++;

  			int count = 1;    // quantidade de [
  			for(i = 0; count != 0; i++){

  				if(*line == '[')
  					count++;
  				if(*line == ']')
  					count--;

  				token[i] = *line;
  				line++;
  			}
  			token[i-1] = '\0';	
  			
  			STACK *new = new_stack();
  			new = eval(token, letras, new);
  			push_arrays(s, new);
		}											/////////////////////




		if(*line == '\0' || *line == '\n')
			break;

  		// parte dedicada aos não arrays ou strings			1 2 +
  		if(!isspace(*line)){
  			for(i=0; !isspace(*line) ; i++){
  				token[i] = *line;
  				line++;
  			}
 			token[i] = '\0';
 			tokenizador(s, letras, token);
 		}
  		while(isspace(*line))
  			line++;

  	}
}

/**
* @param line Linha a ser interpretada
* @param letras Stack com as letras
* @param new Stack que representa o array
* @returns Devolve um apontador para uma stack
*/
STACK *eval(char *line, STACK *letras, STACK *new){

	parse2(new, letras, line);

	return new;
}
