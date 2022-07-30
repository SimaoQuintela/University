#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <unistd.h> /* chamadas ao sistema: defs e decls essenciais */
#include <fcntl.h>	/* O_RDONLY, O_WRONLY, O_CREAT, O_* */
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
	char buffer;

	int fifo = open("fifo", O_RDONLY);
	printf("abri o pipe em modo leitura\n");
	
	while(read(fifo, &buffer, 1)){
		write(1, &buffer, 1);
	}



	return 0;
}
