#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <unistd.h> /* chamadas ao sistema: defs e decls essenciais */
#include <fcntl.h> /* O_RDONLY, O_WRONLY, O_CREAT, O_* */
#include <string.h>

#define MAX_BUFF 256
#define READ 0
#define WRITE 1

/**
 * Estrutura com as transformações e informação sobre as mesmas
 */
typedef struct config_file {
	char* transformation;			// transformação
	int current_num_transf;  		// número de transformações a correr 
	int max_exec_transf;			// número máximo de transformações que podem correr do tipo transformation
} config_file;

/**
 * Lista ligada que representa as tasks que estão a correr de momento
 */
typedef struct tasks_running {
	int task_num;					 // número da task
	char pid[10];					 // pid do cliente que envia a task
	int pid_fork; 					 // pid do processo que responde ao pedido do cliente
	char line[128];					 // linha a executar
	char* line_splitted[20];		 // linha a executar partida
	int in_process;					 // 0 -> task por processar 1-> task em processamento
	int fixed_args;					 // número de argumentos fixos da linha a executar 
	int num_args;					 // número de argumentos da linha da linha a executar
  									 // Nota:  O número de transformações a executar calcula-se fazendo num_args - fixed_args
	int priority;					 // prioridade da tarefa
	struct tasks_running *prox_task; // apontador para a próxima task na lista
} *tasks_running;

// variáveis globais
tasks_running tasks = NULL;
config_file conf_file[7];



int remove_task(tasks_running *l , int num_task){
	if((*l)->task_num == num_task) {
        tasks_running temp = (*l);
        (*l) = (*l)->prox_task;
        free(temp);
        return 0;
    }
    tasks_running prev = (*l);
    while(prev->prox_task) {
        tasks_running list = prev->prox_task;
        if(list->task_num == num_task) {
            prev->prox_task = list->prox_task;
            free(list);
            return 0;
        }
        prev = prev->prox_task;
    }
    return 1;
}

tasks_running add_task(tasks_running *tasks, int running_tasks, char input[], int priority, char pid[], int fixed_args, int N, int status){
	tasks_running nova;
	nova = malloc(sizeof(struct tasks_running));

	strcpy(nova->line, input);
	nova->task_num = running_tasks;
	nova->priority = priority;
	nova->in_process = status;
	nova->fixed_args = fixed_args;
	nova->num_args = N;
	nova->prox_task = NULL;
	strcpy(nova->pid, pid);

	int i = 0;
	char* token;
	char* input_aux;
	input_aux = malloc(strlen(input));
	strcpy(input_aux, input);
	
	token = strtok(input_aux, " ");
	while(token != NULL && i<N){
		nova->line_splitted[i] = malloc(strlen(token));
		strcpy(nova->line_splitted[i],token);
		token = strtok(NULL, " ");
		i+=1;
	}
	nova->line_splitted[i] = "\0";


	while(*tasks != NULL && (*tasks)->priority >= priority){
		tasks = &((*tasks)->prox_task);
	}
	nova->prox_task = *tasks;
	*tasks = nova;

	return nova;

}

/*
void print_conf_file(){
	for(int i=0; i<7; i+=1){
		printf("Transf: %s\n", conf_file[i].transformation);
		printf("Num a correr: %d\n", conf_file[i].current_num_transf);
		printf("Max: %d\n", conf_file[i].max_exec_transf);
	}
}
*/

/*
void print_linked_list(tasks_running *tasks){
	tasks_running temp = *tasks;
	while(temp != NULL){
		printf("Linha: %s\n", temp->line);
		printf("Linha partida: ");
		for(int i = 0; i<temp->num_args; i+=1){
			printf("%s ", temp->line_splitted[i]);
		}
		printf("\nPid: %s\n", temp->pid);
		printf("Pid Fork: %d\n", temp->pid_fork);
		printf("Fixed args: %d\n", temp->fixed_args);
		printf("Num args: %d\n", temp->num_args);
		printf("Task #%d\n", temp->task_num);
		printf("Prioridade: %d\n", temp->priority);
		printf("Em processamento: %d\n\n", temp->in_process);
		temp = temp->prox_task;
	}
}
*/

void fill_struct_conf_file(config_file conf_file[], char* path_to_conf_file){
	char buffer[MAX_BUFF];
	int i = 0;
	int line = 0;

	int fd = open(path_to_conf_file, O_RDONLY, 0666);
	if(fd == -1){
		perror("Erro ao abrir o ficheiro de configuração");
	}

	while(read(fd, buffer+i, 1)){
		if( buffer[i] == ' '){
			buffer[i] = '\0'; 
			conf_file[line].transformation = (char *)malloc(sizeof(i));
			strcpy(conf_file[line].transformation,buffer);
			i = 0;
		} else if(buffer[i] == '\n'){
			buffer[i] = '\0';
			conf_file[line].max_exec_transf = atoi(buffer);
			conf_file[line].current_num_transf = 0;
			i = 0;
			line+=1;
		} else {
			i+=1;
		}

	}

	/* print à struct com os valores lidos no config file
	for(int i = 0; i<7; i+=1){
		printf("\nTransformation: %s\nCurrent_num_transf: %d\nMax_exec_transf: %d\n", conf_file[i].transformation, conf_file[i].current_num_transf, conf_file[i].max_exec_transf);
	}
	*/
}


tasks_running find_line_to_execute(char* line){
	tasks_running temp = tasks;

	while(temp != NULL && strcmp(temp->line, line) != 0){
		temp = temp->prox_task;
	}

	return temp;
}

char* cria_transf(char* transf, char* path_transf_folder, char* transformations[], int index){
	int length_path_folder = strlen(path_transf_folder);
	int length_transf = strlen(transformations[index]);

	transf = malloc(sizeof(length_path_folder + length_transf +2));
	strcpy(transf, "./");
	strcpy(transf + 2, path_transf_folder);
	strcpy(transf + 2 + length_path_folder, transformations[index]);

	return transf;
//	printf("%s\n", transf);
}

void transformations(char* line[], int num_args, char* path_transf_folder, int fixed_args){
	
	char *transformations[num_args-fixed_args];
	int num_transfs = num_args-fixed_args;

	char* input_file = malloc(sizeof(line[fixed_args-2]));
	strcpy(input_file, line[fixed_args-2]);

	char* output_file = malloc(sizeof(line[fixed_args-1]));
	strcpy(output_file, line[fixed_args-1]);

//	printf("Input File: %s\n", input_file);
//	printf("Output File: %s\n", output_file);
	
	/**
	 * Coloca no array transformations as transformações a executar
	 */
	for(int i=0; i<(num_args-fixed_args); i+=1){
		transformations[i] = malloc(sizeof(line[i+fixed_args]));
		strcpy(transformations[i],line[i+fixed_args]);
	//	printf("%s\n", transformations[i]);
	}	
	
	int p[num_transfs-1][2];
	char *transf;

//	printf("num transfs: %d\n\n\n", num_transfs);
	for(int i =0; i<num_transfs; i+=1){
		// transf ----> ./SDStore-transf/transformação
		transf = cria_transf(transf, path_transf_folder, transformations, i);
//		printf("Transf: %s\n", transf);
//		printf("Num args: %d\n", num_transfs);
		
		if(num_transfs == 1){
		//	printf("Entrei aqui\n");
			if(fork() == 0){
				int fd = open(input_file, O_RDONLY);
				if(fd == -1){
					perror("erro ao abrir o file de input");
				}
				dup2(fd, READ);
				close(fd);

				int output = open(output_file, O_TRUNC | O_CREAT |  O_WRONLY, 0666);
				if(output == -1){
					perror("erro ao abrir o file de input");
				}
				dup2(output, WRITE);
				close(output);
				execlp(transf, transf, NULL);
				perror("Algo de errado aconteceu");
				_exit(-1);
			} else {
				wait(NULL);
			}				

		} else if(i == 0){
			pipe(p[i]);
			if(fork() == 0){
				int fd = open(input_file, O_RDONLY);
				if(fd == -1){
					perror("erro ao abrir o file de input");
				}
				dup2(fd, READ);
				close(fd);
				close(p[i][READ]);

				dup2(p[i][WRITE], WRITE);
				close(p[i][WRITE]);
				
				execlp(transf, transf, NULL);
				perror("Algo de errado aconteceu");
				_exit(-1);
			} else {
				wait(NULL);
				close(p[i][WRITE]);
			}
		} else if (i == num_transfs-1) {
			if(fork() == 0){
				dup2(p[i-1][READ], READ);
				close(p[i-1][READ]);
				int output = open(output_file, O_CREAT | O_TRUNC |  O_WRONLY, 0666);
				if(output == -1){
					perror("erro ao abrir o file de input");
				}
				dup2(output, WRITE);
				close(output);
				execlp(transf, transf, NULL);
				perror("Algo de errado aconteceu");
				_exit(-1);
			} else {
				wait(NULL);
				close(p[i-1][READ]);
			}
		} else {
			pipe(p[i]);
			if(fork() == 0){
				close(p[i][READ]);
				dup2(p[i-1][READ], READ);
				close(p[i-1][READ]);
				dup2(p[i][WRITE], WRITE);
				close(p[i][WRITE]);
				execlp(transf, transf, NULL);
				perror("Algo de errado aconteceu");
				_exit(-1);
			} else {
				wait(NULL);
				close(p[i-1][READ]);
				close(p[i][WRITE]);
			}
		}
		
	}
}

int getIndice(char* transf){   //funçao auxiliar que apenas nos da o indice de ocorrencia da transformaçao no conf_file[]
	int r;

	if(strcmp(transf, "nop") == 0) r = 0;
	else if(strcmp(transf, "bcompress") == 0) r = 1;
	else if(strcmp(transf, "bdecompress") == 0) r = 2;
	else if(strcmp(transf, "gcompress") == 0) r = 3;
	else if(strcmp(transf, "gdecompress") == 0) r = 4;
	else if(strcmp(transf, "encrypt") == 0) r = 5;
	else if(strcmp(transf, "decrypt") == 0) r = 6;
        else r=-1;

        return r;

}





int available(config_file conf_file[], char* line[], int num_args, int fixed_args){
           
    int i, ind;
	int r=1;
	int arr[7] = {0,0,0,0,0,0,0};   //array onde estará guardado, no respetivo indice da transformaçao, o numero de transformaçoes a executar

	for(i=fixed_args; i<(num_args); i++){
	    ind = getIndice(line[i]);
	    arr[ind]++;  
   
	}
	
	
	for(i=0; i<7; i++){   
		if((conf_file[i].current_num_transf + arr[i]) > conf_file[i].max_exec_transf) {
			r = 0; //se os que estao a correr mais os que queremos correr for maior que o maximo, retorna 0	
			break;
		}
	}

	if(r == 1){
		for(i=0; i<7; i+=1){
			conf_file[i].current_num_transf += arr[i];
		}
	}

	return r;     
}



char* choose_line_to_execute(){
	tasks_running temp = tasks;
	char* line_to_execute = NULL;
	while(temp != NULL){
		if(temp->in_process == 0 && available(conf_file, temp->line_splitted, temp->num_args, temp->fixed_args) == 1){
			line_to_execute = malloc(sizeof(temp->line));
			strcpy(line_to_execute, temp->line);
			temp->in_process = 1;
		//	printf("linha aceite: %s\n", line_to_execute);
			break;
		}
		temp = temp->prox_task;
	}
//	printf("Linha a executar: %s\n", line_to_execute);
	return line_to_execute;
}

void update_struct(tasks_running task, config_file conf_file[]){
	int N = task->fixed_args;
	for(int i=0; i<task->num_args-N; i+=1){
		int indice = getIndice(task->line_splitted[N+i]);
		conf_file[indice].current_num_transf -= 1;
	}

}



int sizeFile(char line[]){
	int fd = open(line, O_RDONLY, 0666);
	if(fd == -1){
		perror("Erro ao abrir o ficheiro");
		return 1;
	}

	int size = lseek(fd, 0, SEEK_END);
	close(fd);
	return size;
}

void status(tasks_running tasks, char pid[], int num_tasks){
	int pipe_pid = open(pid, O_WRONLY, 0666);
	if(pipe_pid == -1){
		perror("Erro ao abrir o pipe com o pid\n");
	}
	//printf("Pronto para escrever\n");

	char buffer[512];

	tasks_running temp = tasks;
	int size = 0;
	while(temp != NULL){
		size += snprintf(buffer + size, MAX_BUFF, "Task #%d: %s\n", temp->task_num, temp->line);
		temp = temp->prox_task;
	}
	//printf("passei por aqui\n");


	write(pipe_pid, buffer, size);



	// escrever as transformações
	for(int i=0; i<7; i+=1){
		char line[MAX_BUFF];
		int tamanho = snprintf(line, MAX_BUFF, "transf %s: %d/%d (running/max)", conf_file[i].transformation, conf_file[i].current_num_transf, conf_file[i].max_exec_transf);
		write(pipe_pid, line, tamanho);
		write(pipe_pid, "\n", 1);
	}



	close(pipe_pid);
}

void child_handler(int signum){
	int pid, status;
	pid = waitpid(-1, &status, WNOHANG);
	tasks_running task;
	if(pid != -1){
		tasks_running temp = tasks;

		while(temp != NULL && temp->pid_fork != pid){
			temp = temp->prox_task;
		}

		if(temp != NULL){
			update_struct(temp, conf_file);
			remove_task(&tasks, temp->task_num);
		}

	}

}

int main(int argc, char *argv[]){

	// dá informação de como se deve arrancar o server caso este seja inicializado incorretamente
	if(argc != 3){
		write(1, "./sdstored config-filename transformations-folder\n", sizeof("./sdstored config-filename transformations-folder\n"));
		return 1;
	}

	char buffer[MAX_BUFF];
	char pid[20];
	char *exec_args[20];

	char* token;
	int i, fixed_args;

	int task_numero = 1;


	fill_struct_conf_file(conf_file, argv[1]);

	if(mkfifo("main_pipe", 0666) == -1){
		perror("Erro ao criar o pipe");
		return 2;
	}
	write(1, "Main pipe criado com sucesso\n", sizeof("Main pipe criado com sucesso\n"));


	signal(SIGCHLD, child_handler); 
	while(1){
		i = 0;

		int rd = open("main_pipe", O_RDONLY, 0666);
		if(rd == -1){
			perror("Erro ao abrir o pipe de leitura");
			return 4;
		}
		while(read(rd, buffer+i, 1) > 0){  
			i+=1;
		}
	    buffer[i] = '\0';
		close(rd);
   		
		int k = 0;
	 	token = strtok(buffer, " ");
        while(token != NULL){
        	exec_args[k] = malloc(strlen(token));
            strcpy(exec_args[k], token);
        	token = strtok(NULL, " ");
        	k++;
        }
        exec_args[k] = "\0";


		int priority;
        char line[MAX_BUFF];
        int num_args;
        if(strcmp(exec_args[1], "status") != 0){
        	int size = 0;
        	for(i=0; i<k-2; i+=1){
        		strcpy(line+size, exec_args[i]);
        		size += strlen(exec_args[i]);
        		strcpy(line+size, " ");
        		size += 1;
        	}
        	strcpy(line+size, exec_args[i]);
        	size += strlen(exec_args[i]);

        	int tamanho = strlen(exec_args[k-1]);

        	strcpy(pid,exec_args[k-1]);
        	pid[tamanho] = '\0';

        	if(k!=3 && strcmp(exec_args[2], "-p") == 0){
        		fixed_args = 6;
        		priority = atoi(exec_args[3]);
        	} else {
        		fixed_args = 4;
        		priority = 0;
        	}
        	num_args = k-1;
        } else {
        	num_args = 2;
        	strcpy(pid, exec_args[2]);
        }

        
	    
	    tasks_running task;
        char *line_to_execute;
        if(num_args!=2){
        	task = add_task(&tasks, task_numero, line, priority, pid, fixed_args, num_args, 0);
        	
        	int pipe_pid = open(task->pid, O_WRONLY, 0666);
			if(pipe_pid == -1){
				perror("Algo de errado aconteceu");
				return 5;
			}
			char pending[10] = "Pending...";
			write(pipe_pid, pending, 10);

        	char* exec_tasks[20];
        	i =0;
        	while( (line_to_execute = choose_line_to_execute()) != NULL){
        		exec_tasks[i] = malloc(strlen(line_to_execute));
        		strcpy(exec_tasks[i], line_to_execute);
        		i++;
        	}

        	int pid_fork;
        	for(int j=0; j<i; j+=1){
				tasks_running temp = find_line_to_execute(exec_tasks[j]);
        		if( (pid_fork = fork()) == 0){
					//printf("Pid: %s\n",temp->pid);
        			//if(task_numero % 2 == 0){
        			//	sleep(5);
        			//}
					char processing[13] = "Processing...";
					write(pipe_pid, processing, 13);

					if(temp != NULL){	
						transformations(temp->line_splitted, num_args, argv[2], fixed_args);
					}

					int sizeInput = sizeFile(temp->line_splitted[temp->fixed_args -2]);
					int sizeOutput = sizeFile(temp->line_splitted[temp->fixed_args-1]);

					char buff[50];
					int size = snprintf(buff, 50, "Concluded (bytes-input: %d, bytes-output: %d)", sizeInput, sizeOutput);
					write(pipe_pid, buff, size);
					close(pipe_pid);

        			_exit(-1);
        		} else {
					close(pipe_pid);
        		    temp->pid_fork = pid_fork;
        		}	
        	}
        	task_numero += 1;
		} else {
			//print_linked_list(&tasks);
        	//print_conf_file();
        	status(tasks, pid, task_numero);
		}
	}

	unlink("main_pipe");
	return 0;
}
