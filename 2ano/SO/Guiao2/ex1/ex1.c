#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

int main(int argc, char *argv[]){

	char buffer[128];
	pid_t pid_processo = getpid();
	pid_t pid_pai_processo = getppid();


	int size = snprintf(buffer, 128, "Pid do processo: %d\nPid do pai: %d\n ", pid_processo, pid_pai_processo);
	write(1, buffer, size);

	return 0;
}