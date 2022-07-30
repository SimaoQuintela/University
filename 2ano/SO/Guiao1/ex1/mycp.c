#include <stdio.h>
#include <sys/types.h>
#include <unistd.h> /* chamadas ao sistema: defs e decls essenciais */
#include <fcntl.h>	/* O_RDONLY, O_WRONLY, O_CREAT, O_* */
#include <errno.h>
#include <string.h>

#define MAX_BUF 1024 * 1024

// mycp
int main(int argc, char *argv[])
{

	printf("argv[0]: %s\n", argv[0]);
	printf("argv[1]: %s\n", argv[1]);
	printf("argv[2]: %s\n", argv[2]);

	// memória estática
	char buffer[MAX_BUF];
	// memória dinâmica
	// char *buffer = malloc(MAX_BUF)
	int fd_origem, fd_destino;

	if ((fd_origem = open(argv[1], O_RDONLY)) == -1)
	{
		printf("Msg: %s, Nr: %d\n", strerror(errno), errno);
		printf("erro no open origem");
		return -1;
	}

	if ((fd_destino = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, 0640)) == -1)
	{
		perror("erro no open destino");
		return -1;
	}

	int bytes_read;

	while ((bytes_read = read(fd_origem, buffer, MAX_BUF)) > 0)
	{
		write(fd_destino, buffer, bytes_read);
	}

	// free buffer
	close(fd_origem);
	close(fd_destino);
}