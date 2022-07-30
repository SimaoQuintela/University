#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char** argv){

	char *exec_args[]={"bzip2","-c",NULL};

	execvp("bzip2",exec_args);

	perror("error executing command");	

	return 0;
}
