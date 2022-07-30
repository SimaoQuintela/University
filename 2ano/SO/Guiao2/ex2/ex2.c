#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

int main(int argc, char *argv[]){
	
	char buffer[128];
	pid_t new_process = fork();
	int status;
	int size;

	if(new_process == 0){
		pid_t filho = getpid();
		pid_t pai = getppid();

		size = snprintf(buffer, 128, "--- Filho ---\nPid: %d\nPid do pai: %d\n", filho, pai);
		write(1, buffer, size);
		_exit(0);
	} else {
		wait(&status);
		pid_t filho = getpid();
		pid_t pai = getppid();

		size = snprintf(buffer, 128,"--- Pai ---\nPid: %d\nPid do pai: %d\n", filho, pai);
		write(1, buffer, size);
	}

	return 0;
}