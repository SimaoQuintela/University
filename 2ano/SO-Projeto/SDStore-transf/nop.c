#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char** argv){

	char *exec_args[]={"cat",NULL};

	execvp("cat",exec_args);

	perror("error executing command");	

	return 0;
}
