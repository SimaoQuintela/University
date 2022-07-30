#include <stdio.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

int main(int argc, char *argv[]){
	int i,size;
	char buffer[128];
	pid_t new_process;
	int status;
	
	for(i=0; i<10; i+=1){
		new_process = fork();
		
		if(new_process == 0){
			pid_t filho = getpid();
			pid_t pai = getppid();

			size = snprintf(buffer, 128, "--- Processo %d ---\nPid: %d\nPid do pai: %d\n\n\n", i+1, filho, pai);
			write(1, buffer, size);
			_exit(0);
		} else {
			wait(&status);
			if(!WIFEXITED(status) || WEXITSTATUS(status))
				return 1;
		}


	}

	return 0;
}