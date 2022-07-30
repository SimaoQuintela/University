#include <unistd.h> // chamadas ao sistema: defs e decls essenciais
#include <fcntl.h>  // O_RDONLY, O_WRONLY, O_CREAT, 0_*
#include <stdio.h>
#define MAX_BUFFER 1024

//mycat
int main(int argc, char const *argv[]){
	char buffer[MAX_BUFFER];
	int bytes_read;

	while((bytes_read = read(0, buffer, MAX_BUFFER)) >0){
		write(1, buffer, bytes_read);
	}

	printf("terminei\n");

	return 0;
}