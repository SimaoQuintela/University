#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h> /* chamadas ao sistema: defs e decls essenciais */
#include <fcntl.h>	/* O_RDONLY, O_WRONLY, O_CREAT, O_* */
#include <stdio.h>
#include <stdlib.h>

#define MAXBUFFER 1024

int main(int argc, char *argv[]){
	int fd[2];
	pipe(fd);
	char buffer[MAXBUFFER];
	int size, status, i=0;
	pid_t pid;

	//father -> son
	if(fork() == 0){
		close(fd[1]);
		
		while(read(fd[0], buffer+i, 1)){
			i+=1;
		}
		buffer[i] = '\0';
	
		write(1, buffer, i);
		_exit(i);
	} else {
		close(fd[0]);
		write(1, "Father said to his son: ", sizeof("Father said to his son: "));
		
		sleep(5);
		write(fd[1], "Friends is the best sitcom ever made", sizeof("Friends is the best sitcom ever made"));
		close(fd[1]);
		
		pid = wait(&status);
		printf("\n[process %d] Exit status: %d\n", pid, WEXITSTATUS(status));
	}
	
	// son -> father
	/*
	if(fork() == 0){
		close(fd[0]);
		write(fd[1], "Hey dad :)\n", sizeof("Hey dad :)\n"));
		close(fd[1]);
		
		_exit(sizeof("Hey dad :)"));
	} else {
		close(fd[1]);
		while(read(fd[0], buffer+i, 1)){
			i+=1;
		}
		close(fd[0]);
		pid = wait(&status);
		printf("My son [process %d] said: %s", pid, buffer);
		printf("Done [process %d]\n", getpid());
	}
	*/

	return 0;
}