#include "stack.h"
void parse(STACK *s, STACK *letras, char *line);
void parse2(STACK *s, STACK *letras, char *line);
STACK *eval(char *line, STACK *letras, STACK *new);
