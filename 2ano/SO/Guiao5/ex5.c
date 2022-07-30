#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h> /* chamadas ao sistema: defs e decls essenciais */
#include <fcntl.h>	/* O_RDONLY, O_WRONLY, O_CREAT, O_* */
#include <stdio.h>
#include <stdlib.h>

#define READ 0
#define WRITE 1

int main(int argc, char *argv[]){
	int fd[2][2];

	if(pipe(fd[0]) == -1){
		perror("Erro na criação do pipe");
		return 1;
	}

	if(fork() == 0){
		close(fd[0][READ]);
		dup2(fd[0][WRITE], 1);
		close(fd[0][WRITE]);

		execlp("grep", "grep", "-v", "^#", "/etc/passwd", NULL);

		perror("Erro no exec de grep");
		_exit(-1);
	}
	close(fd[0][WRITE]);
	wait(NULL);


	pipe(fd[1]);

	if(fork() == 0){
		dup2(fd[0][READ], 0);
		close(fd[0][READ]);

		dup2(fd[1][WRITE], 1);
		close(fd[1][WRITE]);

		execlp("cut", "cut", "-f7", "-d:", NULL);
		perror("Erro no exec de cut");
		_exit(-1);
	}
	close(fd[0][READ]);
	close(fd[1][WRITE]);
	wait(NULL);


	pipe(fd[0]);

	if(fork() == 0){
		dup2(fd[1][READ], 0);
		close(fd[1][READ]);

		dup2(fd[0][WRITE], 1);
		close(fd[0][WRITE]);

		execlp("uniq", "uniq", NULL);
		perror("Erro no exec uniq");
		_exit(-1);
	}
	close(fd[1][READ]);
	close(fd[0][WRITE]);
	wait(NULL);

	if (fork() == 0) {
        dup2(fd[0][READ], STDIN_FILENO);
        close(fd[0][READ]);

        execlp("wc", "wc", "-l", NULL);
        perror("Erro no exec wc");
        _exit(-1);
    }
    close(fd[0][READ]);
    wait(NULL);

	return 0;
}