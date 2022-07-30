#ifndef ___STACK_H___
#define ___STACK_H___

#include <assert.h>



/**
* Struct que enumera os tipos e que vai aplica-los na struct data
*/
typedef enum {
	LONG = 1,	/**< Tipo Long com o valor 1 (2⁰) associado */
	DOUBLE = 2, /**< Tipo Double com o valor 2 (2¹) associado */
	CHAR = 4, 	/**< Tipo Char com o valor 4 (2²) associado */
	STRING = 8,	/**< Tipo String com o valor 8 (2³) associado */
	arrays = 16, /**< Tipo arrays com o valor 16 (2⁴) associado */
} TYPE;

/**
* Uma struct que nos dá os tipos de dados que estamos a usar na stack
*/
typedef struct data {
	TYPE type;		/**< tipos de dados vindos do enum TYPE */

	long LONG;		/**< Tipo long */
	double DOUBLE;	/**< Tipo double */
	char CHAR;		/**< Tipo char */
	char *STRING;	/**< Tipo string */
	struct stack *arrays;	/**< Tipo arrays que é uma stack */
} DATA;

/**
* Struct que define a estrutura da stack, tendo ela uma inicialização com os tipos definidos em data, com uma variável que dá o tamanho e o número de elementos presentes na stack
*/
typedef struct stack{
	DATA *stack;	/**< Tipo da stack */
	int size;		/**< Tamanho da stack */
	int n_elems;	/**< Numero de elementos ao momento na stack */
} STACK;



int has_type(DATA elem, int mask);
STACK *new_stack();
void push(STACK *s, DATA elem);
DATA pop(STACK *s);
DATA top(STACK *s);
DATA penultimo(STACK *s);
void preencheLetras(STACK *letras);
int is_empty(STACK *s);
void print_stack(STACK *s);
void print_stack2(STACK *s);
void imprime(STACK *s);
DATA enesimo(STACK *s, int n);

/**
* Macro que faz a substituicao de texto de acordo com o stack_operation correspondente
*/
#define STACK_OPERATION_PROTO(_type, _name)		\
	void push_##_name(STACK *s, _type val);		\
	_type pop_##_name(STACK *s);


STACK_OPERATION_PROTO(long, LONG)
STACK_OPERATION_PROTO(double, DOUBLE)
STACK_OPERATION_PROTO(char, CHAR)
STACK_OPERATION_PROTO(char *, STRING)
STACK_OPERATION_PROTO(struct stack *, arrays)


#endif
