#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <unistd.h> /* chamadas ao sistema: defs e decls essenciais */
#include <fcntl.h>	/* O_RDONLY, O_WRONLY, O_CREAT, O_* */
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
	char buffer[1];

	int escrita = open("fifo", O_WRONLY);

	while(read(0, buffer, 1)){
		write(escrita, buffer, 1);
	}

	return 0;
}