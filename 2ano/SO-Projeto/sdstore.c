#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h> /* chamadas ao sistema: defs e decls essenciais */
#include <fcntl.h> /* O_RDONLY, O_WRONLY, O_CREAT, O_* */
#include <string.h>
#define MAX_BUFF 100

void status(char pid[]){
	int pipe_pid = open(pid, O_RDONLY, 0666);
	//printf("Tou aberto\n");

	int i = 0;
	char buffer;
	if(pipe_pid == -1){
		perror("Erro ao abrir o main_pipe");
	}
	
	while (read(pipe_pid, &buffer, 1) > 0) {
		write(1, &buffer, 1);
	}


	close(pipe_pid);
	unlink(pid);
}

int sizeFile(char line[]){
	int fd = open(line, O_RDONLY, 0666);
	if(fd == -1){
		perror("Erro ao abrir o ficheiro");
		return 1;
	}

	int size = lseek(fd, 0, SEEK_END);
	close(fd);
	return size;
}


int main(int argc, char *argv[]){
	char buffer[MAX_BUFF];
	char pid[10];
	snprintf(pid,10,"%d\0", getpid());
	
	if(mkfifo(pid, 0666) == -1){
		perror("Erro ao criar o pipe");
	}
	//printf("Pipe com o pid %s aberto\n", pid);

	if(argc == 1){
		int size = snprintf(buffer, MAX_BUFF, "./sdstore status\n./sdstore proc-file <priority> input-filename output-filename transformation-id1 transformation-id2 ...\n");
		write(1, buffer, size);
	} else {
		int wr = open("main_pipe", O_WRONLY, 0666);
		if(wr == -1){
			perror("Erro ao abrir o main_pipe");
			return 3;
		}
	//	printf("Abertura do pipe de escrita com sucesso\n");

		

		int i=0;
		int tamanho=0;
		for(i=0; i<argc-1; i+=1){
			strcpy(buffer+tamanho, argv[i]);
			tamanho += strlen(argv[i]);
			strcpy(buffer+tamanho, " ");
			tamanho += 1;
		}
		strcpy(buffer+tamanho, argv[i]);
		tamanho += strlen(argv[i]);
		// incluir o pid do processo na passagem de informação 
		strcpy(buffer+tamanho, " ");
		tamanho +=1;
		strcpy(buffer+tamanho, pid);		
		tamanho += sizeof(pid);
		
	//	printf("buffer: %s\n", buffer);
		int s = write(wr, buffer, tamanho);
	//	printf("Escrevi no pipe %d bytes\n", s);
		close(wr);

		if(argc != 2){
			int pipe_pid = open(pid, O_RDONLY, 0666);
			char pending[10];
			read(pipe_pid, pending, 10);
			write(1, pending, 10);

			write(1, "\n", 1);

			char processing[13];
			read(pipe_pid, processing, 13);
			write(1, processing, 13);

			write(1, "\n", 1);

			char buff;
			while(read(pipe_pid, &buff, 1) > 0){
				write(1, &buff, 1);
			}
			close(pipe_pid);
		} else {
			
			status(pid);
		}


		
		unlink(pid);
	}


	return 0;
}