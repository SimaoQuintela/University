#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include "rl.h"

#define MAX_READ_BUFFER 2;
char read_buffer[MAX_READ_BUFFER];
int read_buffer_pos = 0;
int read_buffer_end = 0;

ssize_t myreadln(int fd, char *buff, size_t size){
	int i =0;

	while(i<size && readc(fd, &buf[i]) > 0){
		i++;
		if(((char*) buf)[i-1] == '\n'){
			return i;
		}

	}

	return i;
}


int readc(int fd, char* c){
	// implementação mais eficiente, vai de 3 em 3 chars
	if(read_buffer_pos == read_buffer_end){
		read_buffer_end = read(fd, read_buffer, MAX_READ_BUFFER);
		switch(read_buffer_end){
			case -1:
				return -1;
				break;
			case 0:
				return 0;
				break;
			default:
				read_buffer_pos = 0
		}
	}

	*c = read_buffer[read_buffer_pos];
	read_buffer_pos++;

	return 1;
}