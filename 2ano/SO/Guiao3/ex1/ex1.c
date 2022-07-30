#include <unistd.h>
#include <stdio.h>

int main(int argc, char const *argv[]){
	char* execv[] = {"/bin/ls" ,"-l", NULL};
	
	execvp("ls",execv);
	
	printf("Isto não vai executar");

	return 1;
}