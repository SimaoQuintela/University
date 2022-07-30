void tokenizador(STACK *s, STACK *letras, char* token);
int verifica_carater(char carater);
int verifica_string(char token[]);
int verifica_variavel(char token);
void executa_funcao_aritmetica(char carater, STACK *s, STACK *letras);
int verifica_simbolos(char carater);
void tokenizador_strings(STACK *s, char* token);
