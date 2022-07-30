#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <string.h>
#define MAX_BUFFER 1024


int my_system(char *command){
	pid_t pid;
	int i=0, r_value, status;
	char *string;
	char* exec_args[20];

	string = strtok(command, " ");

	while(string != NULL){
		exec_args[i] = string;
		string = strtok(NULL, " ");

		i+=1;
	}

	exec_args[i] = NULL;

	if((pid = fork()) == 0){
		r_value = execvp(exec_args[0], exec_args);
		_exit(r_value);
	} else {
		pid = wait(&status);
		if(WEXITSTATUS(status) == 255){
			printf("[process %d]: erro na execução\n", pid);
		} else {
			printf("[process %d]: tudo bem\n", pid);
		}

	}



}

int main(int argc, char const *argv[]){

	char command1[] = "ls -l";
	char command2[] = "ps";
	char command3[] = "man system";
	

	my_system(command1);
	my_system(command2);
	my_system(command3);

	return 0;
}