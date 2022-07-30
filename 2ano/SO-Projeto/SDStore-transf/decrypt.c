#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int main(int argc, char** argv){

	char *exec_args[]={"ccrypt","-d","-K","123456",NULL};

	execvp("ccrypt",exec_args);

	perror("error executing command");	

	return 0;
}
