#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h> /* chamadas ao sistema: defs e decls essenciais */
#include <fcntl.h>	/* O_RDONLY, O_WRONLY, O_CREAT, O_* */
#include <stdio.h>
#include <stdlib.h>

#define MAXBUFFER 1024

int main(int argc, char *argv[]){
	
	pid_t pid;
	char buffer[MAXBUFFER];
	int i=0, status;
	int fd[2];
	pipe(fd);

	if(fork() == 0){
		close(fd[1]);
		while(read(fd[0], buffer+i, 1)){
			i+=1;
		}
		
		close(fd[0]);
		_exit(i);
	} else {
		close(fd[1]);
		close(fd[0]);
		pid = wait(&status);
		printf("[process %d] Exit status: %d\n", pid, WEXITSTATUS(status));
		printf("[process %d] Done\n", getpid());
	}


	return 0;
}