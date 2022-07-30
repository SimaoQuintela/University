#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

int main(int argc, char *argv[]){
	char buffer[128];
	int size, status, i;
	pid_t pid;

	for(i=1; i<=10; i+=1){
		pid = fork();
		if(pid == 0){
			pid_t filho = getpid();
			pid_t pai = getppid();

			size = snprintf(buffer, 128, "Processo %d\nPid: %d\nPid do pai: %d\n\n", i, filho, pai);
			write(1, buffer, size);
			_exit(i);
		}
	}

	for(i=1; i<=10; i+=1){
		pid = wait(&status);
		size = snprintf(buffer, 128, "Processo %d terminado\n", pid);
		write(1, buffer, size);

		// se o filho retornou então WIFEXITED retorna "True"
		// se o filho retornou -1 então WIFEXITED retorna "True" e WEXITSTATUS retorna
		// -1 é representado como 255
		if(WIFEXITED(status)){
			printf("[pai] process %d exited. exit code: %d\n", pid, WIFEXITED(status));
		} else {
			printf("[pai] process %d exited.\n", pid);
		}

	}


	return 0;
}