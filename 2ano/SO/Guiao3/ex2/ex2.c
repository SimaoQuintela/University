#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>

int main(int argc, char const *argv[]){
		
	pid_t pid;
	int status;

	if((pid = fork()) == 0){
		execlp("./ex1", "ex1", NULL);
		_exit(-1);
	} else {
		pid = wait(&status);
		if(WEXITSTATUS(status) == 255)
			printf("[process %d]: ocorreu um erro\n", pid);
		else 
			printf("[process %d]: tudo bem\n", pid);
	}
 
	return 0;
}