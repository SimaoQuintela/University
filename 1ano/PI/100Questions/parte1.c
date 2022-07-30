#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <ctype.h>

//1     Returns the biggest element of the sequence
int one(){
    // declarando variáveis
    int maior = 0;
    int n;
    
    printf("Insira os numeros que desejar\n");
    while(n > 0){
        assert(scanf("%d", &n)==1);
        if (n >= maior)
            maior = n;
    }
    return maior;
}

//2  Returns the average of the sequence

void two(){
    int i = 0;
    float soma = 0;
    int numero;
    float media;

    while(numero != 0){
        printf("Insira um numero: ");
        scanf("%d", &numero);
        
        if (numero == 0)
            break;

        soma += numero;
        i++;
    }

    media = soma / i;

    printf("Media: %.2f", media);
}

//3  Return the second biggest of the sequence 
void three(){
    int first = 0,
        second = 0,
        number;

    while(number!= 0){
        printf("Insira um numero: ");
        scanf("%d", &number);

        if(number > first){
            second = first;
            first = number;
        } else if (number > second)
            second = number;

    }

    printf("Second: %d", second);
}

//4  Returns the number of 1's of a binary number represented in decimal by 'n'
void bitsUm(unsigned int n){
    int one = 0;

    while(n!=0){
        if (n%2 == 1)
            one++;
        n = n / 2;
    }

    printf("Number of 1's: %d", one);
}

//5 The opposite of the previous function
int trailingZ(unsigned int n){
    int zero = 0;

    while(n!=0){
        if(n%2==0)
            zero++;
        n /= 2;
    }
    return zero;
}

//6 counts how many digits you need to write the number

int qDig(unsigned int n){
    int i = 0;

    while(n!= 0){
        i++;
        n /= 10;
    }
    return i;
}

//7 concatenate 2 strings 

char *mystrcat (char s1[], char s2[]){
    char newstr[strlen(s1) + strlen(s2)];
    int i, j;

    for (i = 0; i < strlen(s1); i++){
        newstr[i] = s1[i];
    }

    for (j = 0; j < strlen(s2); j++){
        newstr[i + j] = s2[j];
    }

    newstr[strlen(s1) + strlen(s2)] = '\0';

    printf("%s\n", newstr);

    return newstr;
}

//8 

char *mystrcpy(char *dest, char s2[]){
    int i;

    for(i=0; s2[i]!='\0'; i++){
        dest[i] = s2[i];
    }
    dest[i]= '\0';

    return dest;
}

//9 A function that compares 2 strings

int mystrcmp(char s1[], char s2[]) {
    int i = 0, 
        p,
        q;
        
    while(s1[i] == s2[i] && s1[i])
        i++;
        
    p = s1[i];
    q = s2[i];
    return p - q;
}

//10. Fixed 
// "anagrama" "ama"
char *mystrstr(char s1[], char s2[]){
    
    if(*s1 == '\0' && *s2 == '\0')          // "" "" case
		return s1;
    
    if(*s1 == '\n' && *s2 == '\0')          // "\n" "" case (???)
        return s1;
    
	for( ; *s1 ; s1++ ){
		if(*s1 == *s2){
			char *r = s1;
			char *p = s2;
			while(*s1 == *p && *s1){
				p++;
				s1++;
			}

			if(*p == '\0')
				return r;
				
		}
	}


	return NULL;
}

//11 reverse a string

void mystrrev(char s[]){
    int i = strlen(s) - 1, j;
    char s2[strlen(s)];

    for(j=0; j<strlen(s); j++){
        s2[j] = s[i];
        i--;
    }
    s2[j] = '\0';
    printf("%s\n", s2);
}

//12   delete all of the vowels of a string

int contaVogais(char s[]){
    int vogais = 0, i = 0;
    while(s[i]){
        if(s[i]=='a' || s[i]=='A' || s[i]=='e' || s[i]=='E' || s[i]=='i' || s[i]=='I' || s[i]=='o' || s[i]=='O' || s[i]=='u' || s[i]=='U'){
            vogais++;
            i++;
        } else {
            i++;
        }
    }
    return vogais;
}

void strnoV(char s[]){
    int i = 0, j = 0;
    char s2[strlen(s) - contaVogais(s)];

    while(s[i]){
        if(s[i]=='a' || s[i]=='A' || s[i]=='e' || s[i]=='E' || s[i]=='i' || s[i]=='I' || s[i]=='o' || s[i]=='O' || s[i]=='u' || s[i]=='U'){
            i++;
        } else {
            s2[j] = s[i];
            j++;
            i++;
        }
    }
    s2[j] = '\0';

}
// 13
void truncW(char t[], int N){
    int i, j = 0, n=0;

    for(i=0; t[i]; i++){
        if(t[i] == ' '){
            n = 0;
            t[j] = t[i];
            j++;
        } else {
            if (n < N){
                t[j] = t[i];
                j++;
                n++;
            }
        }
    }
    t[j] = '\0';
}

//14    returns the char that appears most often in a string
char charMaisfreq(char s[]){
    int i=0, maior = 0, count, j;
    char maisFreq = s[i];
    
    for(i=0; s[i]; i++){
        count = 0;
        for(j=0; s[j]; j++){
            if (s[i] == s[j])
                count++;
            }
        if(count > maior){
            maior = count;
            maisFreq = s[i];
        }
    }

    printf("%c", maisFreq);

    return maisFreq;
}



//15    return the length of the largest sequence of the same number
int iguaisConsecutivos(char s[]){
    int maior = 0;
    int count = 1;
    int i=0;

    while(s[i]){
        while(s[i]==s[i+1]){
            count++;
            i++;
        }
        if(count >= maior)
            maior = count;
        count=1;
        i++;
    }

    printf("%d",maior);

    return maior;
}

//16    the opposite of the previous one
int difConsecutivos (char s[]){
    int maior = 0, i = 0, count; 

    while(s[i]){
        count = 1;
        while(s[i] != s[i+1]){
            count++;
            i++;
        }
        if(count >= maior)
            maior = count;
        i++;
    }
    
    printf("%d", maior);

    return maior;
}

//17 the biggest prefix between 2 strings
int maiorPrefixo(char s1[], char s2[]){
    int i, count = 0;

    for(i=0; s1[i]; i++){
        if(s1[i] == s2[i])
            count++;
        else
            return count;
    }
    return count;
}

//18 the opposite of the previous one
int maiorSufixo (char s1 [], char s2 []) {
    int i = strlen(s1) -1;
    int j = strlen(s2) -1;
    int count = 0;
    
    while(i>=0){
        if(s1[i] == s2[j]){
            count++;
            i--;
            j--;
        } else 
            return count;
    }
    return count;
}
// 19 returns the number of characters that sufix and prefix of 2 words has in common
int sufPref(char s1[], char s2[]){
    int count = 0, j = 0, i;

    for(i=0; s1[i]; i++){
        if(s1[i] == s2[j]){
            count++;
            j++;
        } else {
            count = 0;
            j = 0;
        }
    }
    return count;
}

// 20 counts how many words a string has
int contaPal(char s[]){
    int count = 0, i = 0;

    while(i<strlen(s)){
        if(!(isspace(s[i])) && s[i] != '\n'){   // aldrabei um bocadito com o \n
            count++;
            i++;
        }
        while(!(isspace(s[i]))){
            i++;
        }
        while(isspace(s[i])){
            i++;
            }
        }
    return count;
}

// 21 counts how many vowels a string has
int contaVogais(char s[]){
    int i , count = 0;

    for(i=0; s[i]; i++){
        if (s[i]=='a' || s[i]=='A' || s[i]=='e' || s[i]=='E' || s[i]=='i' || s[i]=='I' || s[i]=='o' || s[i]=='O' || s[i]=='u' || s[i]=='U')
            count++;
    }
    return count;
}


// 22 return true (1) if all of the chars of the first string are contained on the second string, else return False (0)
int verifica_se_faz_parte(char carater, char b[]){
    int i, faz_parte = 0;

    for(i=0; b[i]; i++){
        if(carater == b[i])
            faz_parte = 1;
    }

    return faz_parte;
}

int contida (char a[], char b[]){
    int i;
    int resultado = 0;

    for(i=0; a[i]; i++){
        if (verifica_se_faz_parte(a[i], b) == 0){
            resultado = 0;
            break; 
        } else 
            resultado = 1;
        
    }

    return resultado;
}

// 23.
int palindrome(char s[]){
    int i, j = strlen(s)-1, result = 1;


    for(i=0; i < (strlen(s)/2) ; i++){
        if(s[j] == s[i])
            j--;
        else{
            result = 0;
            break;  // desculpa jbb eu sei que não gostas dos breaks mas neste caso ele é descartável, só o pus para isto andar mais depressa :)
        }
    }

    return result;
}

//24.
int remRep(char s[]){
    int i, j;

    for(i=0; s[i]; i++){
        if(s[i] == s[i+1]){
            for(j=i+1; s[j]; j++)
                s[j] = s[j+1];
            i--;
        }
    }

    return i;
}

//25. 
int limpaEspacos(char t[]){
    int i, j;

    for(i=0; s[i]; i++){
        if(s[i] == ' ' && s[i+1] == ' '){
            for(j=i+1; s[j]; j++)
                s[j] = s[j+1];
            i--;
        }
    }
    return i;
}

//26
int insere(int v[], int N, int x){
    int i, j;

    for(i=0; v[i]; i++){
        if(v[i] > x){
            for(j=N; j>i; j--){
                v[j] = v[j-1];
            }
            v[i] = x;
            break;
        }
        if(i == N - 1) {
            v[N] = x;
        }
    }
}

//27.
void merge (int r [], int a[], int b[], int na, int nb){
    int i=0, j=0, k;

    for(k=0; i<na && j<nb; k++){
        if(a[i] < b[j]){
            r[k] = a[i];
            i++;
        } else {
            r[k] = b[j];
            j++;
        }
    }
            
    while(i<na){
        r[k] = a[i];
        k++;
        i++;
    }

    while(j<nb){
        r[k] = b[j];
        k++;
        j++;
    }
}

//28.
int crescente(int a[], int i, int j){
    int resultado = 1;

    while(i!=j){
        if(a[i] > a[i+1])
            resultado = 0;
        i++;
    }

    return resultado;
}

//29.
int retiraNeg(int v[], int N){
    int i = 0, j;

    while(i<N){
        if(v[i] < 0){
            for(j=i; j<N-1; j++)
                v[j] = v[j+1];           
            N--;
        } else 
            i++;
    }

    return N;
}

//30.
int contaRepetidos(int numero, int v[], int N){
    int i=0, count=0;

    while(i<N){
        if(numero == v[i])
            count++;
        i++;
    }

    return count;
}


int menosFreq (int v[], int N){
    int i=0, resultado = v[i];

    int menor = contaRepetidos(v[i], v, N);
    
    while(i<N){
        int x = contaRepetidos(v[i], v, N);
        if(x<menor){
            menor = x;
            resultado = v[i];
        }
        i+=x;
    }

    return resultado;
}

//31.
int contaRepetidos(int numero, int v[], int N){
    int i=0, count=0;

    while(i<N){
        if(numero == v[i])
            count++;
        i++;
    }

    return count;
}


int maisFreq (int v[], int N){
    int i=0, resultado = v[i];

    int maior = contaRepetidos(v[i], v, N);
    
    while(i<N){
        int x = contaRepetidos(v[i], v, N);
        if(x>maior){
            maior = x;
            resultado = v[i];
        }
        i+=x;
    }

    return resultado;
}

//32.
int maxCresc(int v[], int N){
    int i, maior = 1, r = 1;

    for(i=0; i<N; i++){
        if(v[i+1] >= v[i])
            r++;
        else {
            if(r>maior)
                maior = r;
            r=1;
        }
    }
    return maior;
}


//33.
int pertence(int v[], int x, int N){
    int i = 0; 
    int r = -1;		// se repetir apenas 1 vez vai ficar 1, senão vai ficar > 1
    
    while(i<N){
        if(v[i] == x){
            r++;
            i++;
        } else 
            i++;
    }
    
    if(r>=1)
        return 1;
    else
        return 0;
}

int elimRep(int v[], int N){
    int i, j;
    
    for(i=0; i<N; i++){
        while(pertence(v, v[i], N) >= 1){
            j=i+1;
            while(j<N){
                if(v[j] == v[i]){
                    while(j<N){
                        v[j] = v[j+1];
                        j++;
                    }
                } else 
                    j++;
            }
            N--;
        }
    }
    return N;
}



//34.
int elimRepOrd (int v[], int n){
    int i=0, j;

    while(i<n-1){
        if(v[i] == v[i+1]){
            for(j=i; j<n; j++)
                v[j] = v[j+1];
            n--;
        } else
            i++;
    }
    return n;
}
//35.
int comunsOrd(int a[], int na, int b[], int nb){
    int i=0, j=0, count = 0;

    while(i<na && j<nb){
        if(a[i] == b[j]){
            count++;
            i++;
            j++;
        } else {
            if(a[i] < b[j])
                i++;
            else 
                j++;
        }
    }
    return count;
}

//36.
int pertence(int b[], int number, int nb){
    int i = 0, r = 0;

    while(i<nb){
        if(b[i] == number){
            r = 1;
            break;
        }
        i++;
    }

    return r;
}

int comuns(int a[], int na, int b[], int nb){
    int i, count = 0;

    for(i=0; i<na;i++){
        if(pertence(b, a[i], nb))
            count++;
    }

    return count;
}

//37.
int minInd(int v[], int n){
    int i, indice = 0;

    for(i=0; i<n; i++){
        if(v[i] <= v[indice])
            indice = i;
    }

    return indice;
}

//38.
int somaAte(int v[], int indice){
    int i, resultado = 0;

    for(i=0; i<=indice; i++){
        resultado += v[i];
    }

    return resultado;
}

void somasAc(int v[], int Ac[], int N){
    int i;

    for(i=0; i<N; i++){
        Ac[i] = somaAte(v, i);
    }
}

//39. 
int triSup(int N, float m[N][N]){
    int i, j, r = 1;

    for(i=1; i<N; i++){
        for(j=0; j<i; j++){
            if(m[i][j] != 0)
                r = 0;
        }
    }

    return r;
}

//40.
void transposta(int N, float m[N][N]){
    int i, j;
    float m_aux[N][N];


    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            m_aux[j][i] = m[i][j];
        }
    }

    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            m[i][j] = m_aux[i][j];
        }
    }    
}

// usando a técnica do swap
void transposta (int N, float m [N][N]) {
    int i, j;
    float temp;
    
    for(i=1; i<N; i++){
        for(j=0; j<i; j++){
            temp = m[i][j];
            m[i][j] = m[j][i];
            m[j][i] = temp;
        }
    }
}


//41. 
void addTo(int N, int M, int a[N][M], int b[N][M]){
    int i, j;

    for(i=0; i<N; i++){
        for(j=0; j<M; j++){
            a[i][j] += b[i][j];
        }
    }
}


//42.
int unionSet (int N, int v1[N], int v2[N], int r[N]){
    int i;
    for (i = 0; i < N; i++)
        r[i] = v1[i] || v2[i];
    return i;
}

//43.
int intersectSet (int N, int v1[N], int v2[N], int r[N]){
    int i;
    for (i = 0; i < N; i++)
        r[i] = v1[i] && v2[i];
    return i;
}

//44.


//45.


//46. 
int cardinalMSet (int N, int v[N]){
    int i, res = 0;
    
    for(i=0; i<N; i++)
        res += v[i];
    
    return res;
}

//47.
typedef enum movimento {
    Norte,
    Oeste,
    Sul,
    Este
} Movimento;

typedef struct posicao {
    int x, y;
} Posicao;


Posicao posFinal (Posicao inicial, Movimento mov[], int N){
    int i;

    for(i=0; i<N; i++){
        switch(mov[i]){
            case Norte: inicial.y++;
                break;
            case Oeste: inicial.x--;
                break;
            case Sul: inicial.y--;
                break;
            case Este: inicial.x++;
                break;
        }
    }
    return inicial;
}

//48.
int caminho(Posicao inicial, Posicao final, Movimento mov[], int N){
    int i, r = 0;

    for(i=0; i<N && (inicial.x != final.x || inicial.y != final.y); i++){
        if(inicial.x > final.x){
            mov[i] = Oeste;
            inicial.x--;
            r++;
        } else if(inicial.x < final.x){
            mov[i] = Este;
            inicial.x++;
            r++; 
        } else if(inicial.y > final.y){
            mov[i] = Sul;
            inicial.y--;
            r++;
        } else if(inicial.y < final.y){
            mov[i] = Norte;
            inicial.y++;
            r++;
        }
    }

    if(inicial.x != final.x || inicial.y != final.y)
        r = -1;

    return r;
}

//49. Pouco eficiente mas funfa
float hipotenusa(int x, int y){
    float hipotenusa;

    hipotenusa = sqrt(x*x + y*y);

    return hipotenusa;
}

int maiscentral(Posicao pos[], int N){
    int i=0, menor = 0;
    float hip;
    
    hip = hipotenusa(pos[i].x , pos[i].y);

    for(i=1; i<N; i++){
        if(hipotenusa(pos[i].x , pos[i].y) < hip){
            menor = i;
            hip = hipotenusa(pos[i].x , pos[i].y);
        }
    }

    return menor;
}


//50.
int vizinhos(Posicao p, Posicao pos[], int N){
    int i, count = 0;

    for(i=0; i<N; i++){
        if( sqrt(pow((p.x - pos[i].x),2) + pow((p.y- pos[i].y),2)) == 1 ){
            count++;
        }
    }
    return count;
}




int main(){
    int n;

    printf("Insira o numero da pergunta: ");
    scanf("%d", &n);

    switch (n) {
        case 1 : printf("O maior numero e': %d", one());
            break;
        case 2 : two();
            break;
        case 3 : three();
            break;
        case 4 : bitsUm(27);
            break;
        case 5 : printf("Zeros: %d", trailingZ(27));
            break;
        case 6 : printf("Digitos: %d",qDig(456));
            break;
        case 7 : mystrcat("Hello", "World");
            break;
        case 9 : printf("Resultado: %d", strcmp("Hello", "Helloo"));
            break;
        case 10 : mystrstr("anagrama","ama");
            break;
        case 11 : mystrrev("ana");  // badum ts
            break;
        case 12 : strnoV("jota be be");
            break;
    }   

    return 0;
}
