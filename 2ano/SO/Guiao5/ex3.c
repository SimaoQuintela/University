#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h> /* chamadas ao sistema: defs e decls essenciais */
#include <fcntl.h>	/* O_RDONLY, O_WRONLY, O_CREAT, O_* */
#include <stdio.h>
#include <stdlib.h>

#define MAXBUFFER 1024

//dúvidas neste ex
int main(int argc, char  *argv[]){

	int i=0, status, fd[2];
	char buffer[MAXBUFFER];
	char *command;
	pid_t pid;
	pipe(fd);

	if(fork() == 0){
		close(fd[1]);
		dup2(fd[0], 0);
		close(fd[0]);

		execlp("wc", "wc", NULL);

		_exit(-1);

	} else {
		close(fd[0]);
		
		while(read(0, buffer, 1)){
			write(fd[1], buffer, 1);
		}

		close(fd[1]);

		wait(NULL);
		printf("[process %d] Done", getpid());
	}

	return 0;
}