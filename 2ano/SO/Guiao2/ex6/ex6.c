#include <unistd.h>
#include <string.h>
#include <stdio.h>      
#include <stdlib.h>  
#include <sys/wait.h>

//usar a função waitpid 


int main(int argc, char *argv[]){
	srand(atoi(argv[2]));
	int linhas = rand()%10 +1;		   // número random entre 1 e 10
	int colunas = rand()%20;   // número random entre 10 e 29
	int matriz[linhas][colunas];
	
	int size;
	char buffer[128];

	size = snprintf(buffer, 128,"Matriz %d por %d\n", linhas, colunas);
	write(1, buffer, size);


	// preencher a matriz random
	for(int i=0; i<linhas; i+=1){
		for(int j=0; j<colunas; j+=1){
			matriz[i][j] = rand()%10;
			printf("%d   ", matriz[i][j]);
		}
		printf("\n");

	}

	int findMe = atoi(argv[1]);
	int status;
	pid_t pid;
	pid_t array_de_pids[10];
	
	// procurar o número na matriz
	for(int i=0; i<linhas; i++){
		if((pid = fork()) == 0){
			for(int j=0; j<colunas; j++){
				if(matriz[i][j] == findMe){
					_exit(i);
				}
			}
				
			_exit(-1);
		} else {
			array_de_pids[i] = pid;
		}
	}



	for(int i = 0; i<linhas; i++){
		pid = wait(&status);
		if(WEXITSTATUS(status) == 255) // quando dá return -1
			printf("[Process: %d] Não encontrei nada\n", pid);
		else{
			printf("[Process: %d] Encontrei o numero %d na linha %d\n", pid, findMe, WEXITSTATUS(status));
		}
	}

	return 0;
}