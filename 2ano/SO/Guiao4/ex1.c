#include <stdio.h>
#include <sys/types.h>
#include <unistd.h> /* chamadas ao sistema: defs e decls essenciais */
#include <fcntl.h>	/* O_RDONLY, O_WRONLY, O_CREAT, O_* */

// redirecionar stdin para /etc/passwd
// redirecionar stdout e stderror para saida.txt e erros.txt, resp.

int main(int argc, char const *argv[]){
	char buffer[512];
	ssize_t n_read;

	int savefs = dup(1);
	
	int fi = open("/etc/passwd", O_RDONLY, 0666);
	int fs = open("saida.txt", O_CREAT | O_TRUNC | O_WRONLY, 0666);
	int fe = open("erros.txt", O_CREAT | O_TRUNC | O_WRONLY, 0666);

	
	dup2(fi, 0); // stdin a apontar para fi
	dup2(fs, 1); // stdout a apontar para fs
	dup2(fs, 2); // stderror a apontar para1 fe

	close(fi);
	close(fs);
	close(fe);

	while( n_read = read(0, buffer, sizeof(buffer)) ){
		write(1, buffer, n_read);
		write(2, buffer, n_read);
	}


	dup2(savefs, 1);

	write(1, "terminei\n", sizeof("terminei\n"));


	return 0;
}