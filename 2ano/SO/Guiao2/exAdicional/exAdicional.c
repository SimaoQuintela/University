#include <unistd.h>
#include <string.h>
#include <stdio.h>      
#include <fcntl.h>
#include <stdlib.h>  
#include <sys/wait.h>


int main(int argc, char *argv[]){
	srand(atoi(argv[2]));
	int linhas = rand()%10 +1;		   // número random entre 1 e 10
	int colunas = rand()%20;   // número random entre 10 e 29
	int matriz[linhas][colunas];
	int i, j;
	int size;
	char buffer[128];

	size = snprintf(buffer, 128,"Matriz %d por %d\n", linhas, colunas);
	write(1, buffer, size);

	// preencher a matriz random
	for(i=0; i<linhas; i+=1){
		for(j=0; j<colunas; j+=1){
			matriz[i][j] = rand()%10;
			printf("%d   ", matriz[i][j]);
		}
		printf("\n");
	}

	// escrever a matriz no ficheiro 
	int fd = open("matriz.txt", O_WRONLY, 0666);
	if( write(fd, matriz, sizeof(matriz)) == -1)
		return 1;
	close(fd);

/* ----------- procurar o número na matriz ------------- */
	pid_t pid;
	int findMe = atoi(argv[1]);
	int linha[colunas];
	int status;

	for(i=0; i<linhas; i+=1){
		if( (pid = fork()) == 0){
			fd = open("matriz.txt", O_RDONLY, 0666);
			lseek(fd, i*colunas*sizeof(int), SEEK_SET);
			read(fd, &linha, sizeof(linha));
			
			for(j=0; j<colunas; j+=1)
				if(linha[j] == findMe){
					close(fd);
					_exit(i);
				}
			close(fd);
			_exit(-1);	
		}
	}


	for(i=0; i<linhas;i+=1){
		pid = wait(&status);
		if(WEXITSTATUS(status) == 255){
			printf("[process %d] Não encontrei nada\n", pid);
		} else {
			printf("[process %d] Encontrei na linha %d\n", pid, WEXITSTATUS(status));
		}
	}

/* visualizar a matriz escrita no ficheiro */
	fd = open("matriz.txt", O_RDONLY, 0666);
	for(i=0;i<linhas;i+=1){
		read(fd, &linha, sizeof(linha));
		for(j=0;j<colunas;j+=1){
			printf("%d   ", linha[j]);
		}
		printf("\n");
	}



	return 0;
}