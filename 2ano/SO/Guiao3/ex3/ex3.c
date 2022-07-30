#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>

int main(int argc, char const *argv[]){
	pid_t pid;
	int status;


	for(int i=1; i<argc; i+=1){
		if( (pid = fork()) == 0){
			execlp(argv[i], argv[i], NULL);
			exit(-1);
		}
	}

	for(int i=1; i<argc; i+=1){
		pid = wait(&status);
		if(WEXITSTATUS(status) == 255)
			printf("[process %d]: ocorreu um erro\n", pid);
		else
			printf("[process %d]: tudo ok\n", pid);

	}


	return 0;
}