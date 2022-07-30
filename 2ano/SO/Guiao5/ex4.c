#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h> /* chamadas ao sistema: defs e decls essenciais */
#include <fcntl.h>	/* O_RDONLY, O_WRONLY, O_CREAT, O_* */
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
	int fd[2];

	if(pipe(fd) == -1){
		perror("Erro na criação do pipe\n");
		return 1;
	}

	if(fork() == 0){
		close(fd[0]);
		dup2(fd[1], 1);
		close(fd[1]);

		execlp("ls", "ls", "/etc", NULL);
		_exit(-1);
	}
	close(fd[1]);
	wait(NULL);

	if(fork() == 0){
		dup2(fd[0], 0);
		close(fd[0]);
		
		execlp("wc", "wc", "-l", NULL);	
		_exit(-1);
	}
	close(fd[0]);
	wait(NULL);

	return 0;
}