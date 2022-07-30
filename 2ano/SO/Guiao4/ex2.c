#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h> /* chamadas ao sistema: defs e decls essenciais */
#include <fcntl.h>	/* O_RDONLY, O_WRONLY, O_CREAT, O_* */
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
	char buffer[512];
	ssize_t n_bytes;
	int status;

	pid_t pid = fork();

	if(pid == 0){
		int save_stdout = dup(1);

		int file_read = open("/etc/passwd", O_RDONLY, 0666);
		int file_saida = open("saida.txt", O_CREAT | O_TRUNC | O_WRONLY, 0666);
		int file_erro = open("erros.txt", O_CREAT | O_TRUNC | O_WRONLY, 0666);

		dup2(file_read, 0);
		dup2(file_saida, 1);
		dup2(file_erro, 2);

		close(file_read);
		close(file_saida);
		close(file_erro);

		while( n_bytes = read(0, buffer, sizeof(buffer)) ){
			write(1, buffer, sizeof(buffer));
			write(2, buffer, sizeof(buffer));
		}
			write(1, "\n", sizeof("\n"));
			write(2, "\n", sizeof("\n"));

		// não preciso de fazer isto para o pai imprimir no stdout
		// simplesmente fiz isto para ganhar agilidade no redirecionamento
		// de descritores
		dup2(save_stdout, 1);
		write(1, "De volta ao stdout\n", sizeof("De volta ao stdout\n"));

		_exit(EXIT_SUCCESS);
	} else {
		pid_t pid = wait(&status);
		if(WEXITSTATUS(status) == 255){
			printf("[process %d] ocorreu um problema\n", pid);
		} else {
			printf("[process %d] tudo ok\n", pid);
		}
	}

	printf("Terminei\n");
	
	return 0;
}