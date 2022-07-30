#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h> /* chamadas ao sistema: defs e decls essenciais */
#include <fcntl.h>	/* O_RDONLY, O_WRONLY, O_CREAT, O_* */
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
	int fd = open(argv[2], O_RDONLY, 0666);
	dup2(fd, 0);

	close(fd);

	pid_t pid;
	int status;

	if( (pid = fork()) == 0 ){
		execlp("wc", "wc", "/etc/passwd", NULL);
		_exit(-1);
	} else {
		pid = wait(&status);
		if(WEXITSTATUS(status) == 255){
				printf("[process %d] ocorreu um problema\n", pid);
		} else {
			printf("[process %d] tudo ok\n", pid);
		}

	}

	printf("Terminei\n");

	return 0;
}