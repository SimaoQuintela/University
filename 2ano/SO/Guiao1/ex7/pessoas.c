#include "pessoas.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#define MAX_BUF 1024


//Estou a assumir em toda a ficha que os nomes dados não são repetidos e que
//na posição que dão há, de facto, um nome 

int new_person(char* name, int age){
	Person p;
	int counter = 1;
	char string_buff[50];


	int fd = open("pessoas.txt", O_RDWR, 0777);

	if(fd == -1)
		perror("An error has ocurred");
	else {
		while(read(fd, &p, sizeof(p)) > 0)
			counter += 1;

		int size = snprintf(string_buff, 50, "registo %d\n", counter);
		// 1- writes on terminal 
		write(1, string_buff, size);
		
		p.age = age;
		strcpy(p.name, name);
		// fd- writes on file dest
		write(fd, &p, sizeof(p));

	}
	
	close(fd);
	return 0;
}

int person_change_age_v2(long pos, int age){
	Person p;
	int fd = open("pessoas.txt", O_RDWR, 0777);


	lseek(fd, (pos)*sizeof(p), SEEK_SET);
	lseek(fd, -sizeof(p), SEEK_CUR);
	read(fd, &p, sizeof(p));
	p.age = age;
	lseek(fd, -sizeof(p), SEEK_CUR);
	write(fd, &p, sizeof(p));



	close(fd);
	return 0;

}

/*
resolução menos eficiente porque se tem de percorrer o ficheiro todo
até chegar à posição pretendida

int person_change_age_v2(long pos, int age){
	Person p;
	int counter = 1;

	int fd = open("pessoas.txt", O_RDWR, 0777);
	
	while( read(fd, &p, sizeof(p)) > 0 ){
		if(counter == pos){
			p.age = age;
			lseek(fd, -sizeof(p), SEEK_CUR);
			write(fd, &p, sizeof(p));
		}
		counter += 1;
	}

	close(fd);
	return 0;
}
*/

int main(int argc, char *argv[]){
		
	if(strcmp(argv[1], "-i") == 0){
		new_person(argv[2], atoi(argv[3]));
	} else if(strcmp(argv[1], "-o") == 0){
		person_change_age_v2(atoi(argv[2]), atoi(argv[3]));
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