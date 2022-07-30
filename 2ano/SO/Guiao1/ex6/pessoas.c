#include "pessoas.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
// ver função atoi no google
#define MAX_BUF 1024

int new_person(char* name, int age){
	Person p;
	p.age = age;
	strcpy(p.name, name);

	int fd = open("pessoas.txt",O_APPEND | O_WRONLY, 0777);

	if(fd == -1)
		perror("An error has ocurred");
	else
		write(fd, &p, sizeof(p));
	
	close(fd);

	return 0;
}


int person_change_age(char* name, int age){
	char buff[MAX_BUF];

	int fd = open("pessoas.txt", O_RDWR, 0554);
	int found = 0, n;

	Person p;
	while(n =read(fd, &p, sizeof(p)) > 0)
		if(strcmp(p.name, name) == 0){
			printf("Name found!\n");
			found = 1;
			p.age = age;
			lseek(fd, -sizeof(p), SEEK_CUR);
			write(fd, &p, sizeof(p));
			close(fd);
			return 0;
		}
	

	if(n == -1)
		printf("Oops. Something went wrong\n");
	

	if(found != 1)
		printf("Name not found\n");
	
	close(fd);
	return -1;
}




int main(int argc, char* argv[]){

	if(strcmp(argv[1],"-i") == 0){
		// supondo que não há pessoas repetidas
		printf("Entrei na flag -i\n");
		new_person(argv[2], atoi(argv[3]));

	} else if(strcmp(argv[1], "-u") == 0){
		printf("Entrei na flag -u\n");
		person_change_age(argv[2], atoi(argv[3]));
	
	}
	

	// ler o conteúdo dos registos
	if(strcmp(argv[1], "-r") == 0){
		int n;
		char buffer[512];
		int fd = open("pessoas.txt", O_RDONLY, 0554);
		Person p;

		while ((n = read(fd, &p, sizeof(p)) > 0)) {
			int x = snprintf(buffer, 512, "name: %s; age: %d\n", p.name, p.age);
			write(1, buffer, x);
		}

		close(fd);

	}

	return 0;
}

