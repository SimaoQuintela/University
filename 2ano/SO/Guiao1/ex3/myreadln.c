#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

ssize_t myreadln(int fd, char *line, size_t size){
	char c;
	ssize_t bytes_read = 0;

	while(read(fd, &c, 1) > 0 && c != '\n'){
		if(bytes_read >= size){
			fprintf(stderr, "not enough space to store that line\n");
			return -1;
		}
		line[bytes_read] = c;
		bytes_read += 1;
	}

	printf("%s", line);

	return bytes_read;
}


int main(int argc, char* argv[]){
	char *line;
	int fd = open(argv[1], O_RDONLY);

	myreadln(fd, line, 100);

}