// ssize_t read(int fildes, void *buf, size_t n_byte);
//					 |			 |			  |
//				lê daqui     mete aqui	
#define FILENAME "file_pessoas"

typedef struct Person{
	char name[200];
	int age;
} Person;



//API
int new_person(char* name, int age);
int person_change_age(char* name, int age); // ex. 6
int person_change_age_v2(long pos, int age); // ex. 7
