#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <unistd.h> /* chamadas ao sistema: defs e decls essenciais */
#include <fcntl.h>	/* O_RDONLY, O_WRONLY, O_CREAT, O_* */
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
	char buffer;

	if(mkfifo("fifo", 0666) == -1){
		perror("Erro ao criar o pipe");
		return 1;
	}
	printf("pipe criado com sucesso\n");

	int log = open("log.txt", O_CREAT | O_WRONLY, 0666);
	if(log == -1){
		perror("Erro ao abrir o ficheiro log");
		return 2;
	}
	
	int rd = open("fifo", O_RDONLY);


	while(read(rd, &buffer, 1)){
		write(log, &buffer, 1);
	}

	close(log);
	unlink("fifo");
	return 0;
}
