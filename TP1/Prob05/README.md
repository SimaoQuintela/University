# 5 Ficheiros CSV com listas e funções de agregação
Neste enunciado pretende-se fazer um conversor de um ficheiro CSV (Comma separated values) para o formato JSON.
Para se poder realizar a conversão pretendida, é importante saber que a primeira linha do CSV dado funciona como
cabeçalho que define o que representa cada coluna.  
Por exemplo, o seguinte ficheiro "alunos.csv":

```
    Número,Nome,Curso
    3162,Cândido Faísca,Teatro
    7777,Cristiano Ronaldo,Desporto
    264,Marcelo Sousa,Ciência Política
```

Corresponde à seguinte tabela:
    Número Nome Curso
    3162 Cândido Faísca Teatro
    7777 Cristiano Ronaldo Desporto
    264 Marcelo Sousa Ciência Política


No entanto, neste trabalho, os **CSV** recebidos têm algumas extensões.


## 5.1 Listas
Nestes datasets, poderemos ter conjuntos de campos que formam listas.

### Listas com tamanho definido
No cabeçalho, cada campo poderá ter um número N que representará o número de colunas que esse campo abrange.
Por exemplo, imaginemos que ao exemplo anterior se acrescentou um campo Notas, com N = 5 ("alunos2.csv"):

Número,Nome,Curso,Notas{5},,,,,
3162,Cândido Faísca,Teatro,12,13,14,15,16
7777,Cristiano Ronaldo,Desporto,17,12,20,11,12
264,Marcelo Sousa,Ciência Política,18,19,19,20,18

Isto significa que o campo Notas abrange 5 colunas. (Reparem que temos de meter os campos que sobram a vazio,
para o **CSV** bater certo).

### Listas com um intervalo de tamanhos
Para além de um tamanho único, podemos também definir um intervalo de tamanhos {N, M }, significando que o
número de colunas de um certo campo pode ir de N até M . ("alunos3.csv")
```
    Número,Nome,Curso,Notas{3,5},,,,,
    3162,Cândido Faísca,Teatro,12,13,14,,
    7777,Cristiano Ronaldo,Desporto,17,12,20,11,12
    264,Marcelo Sousa,Ciência Política,18,19,19,20,
```


## 5.2 Funções de agregação
Para além de listas, podemos ter funções de agregação, aplicadas a essas listas.
Veja os seguintes exemplos ("alunos4.csv" e "alunos5.csv"):
```
    Número,Nome,Curso,Notas{3,5}::sum,,,,,
    3162,Cândido Faísca,Teatro,12,13,14,,
    7777,Cristiano Ronaldo,Desporto,17,12,20,11,12
    264,Marcelo Sousa,Ciência Política,18,19,19,20,
```
```
    Número,Nome,Curso,Notas{3,5}::media,,,,,
    3162,Cândido Faísca,Teatro,12,13,14,,
    7777,Cristiano Ronaldo,Desporto,17,12,20,11,12
    264,Marcelo Sousa,Ciência Política,18,19,19,20,
```
etc.


## 5.3 Resultado esperado
O resultado final esperado é um ficheiro JSON resultante da conversão dum ficheiro CSV.
Por exemplo, o ficheiro "alunos.csv" (original), deveria ser transformado no seguinte ficheiro "alunos.json":
```js
[
    {
        "Número": "3612",
        "Nome": "Cândido Faísca",
        "Curso": "Teatro"
    },
    {
        "Número": "7777",
        "Nome": "Cristiano Ronaldo",
        "Curso": "Desporto"
    },
    {
        "Número": "264",
        "Nome": "Marcelo Sousa",
        "Curso": "Ciência Política"
    }
]
```
No caso de existirem listas, os campos que representam essas listas devem ser mapeados para listas em JSON
("alunos2.csv"):
```js
[
    {
        "Número": "3612",
        "Nome": "Cândido Faísca",
        "Curso": "Teatro",
        "Notas": [12,13,14,15,16]
    },
    {
        "Número": "7777",
        "Nome": "Cristiano Ronaldo",
        "Curso": "Desporto",
        "Notas": [17,12,20,11,12]
    },
    {
        "Número": "264",
        "Nome": "Marcelo Sousa",
        "Curso": "Ciência Política",
        "Notas": [18,19,19,20,18]
    }
]
```

No caso em que temos uma lista com uma função de agregação, o processador deve executar a função associada à
lista, e colocar o resultado no JSON, identificando na chave qual foi a função executada ("alunos4.csv"):
```js
[
    {
        "Número": "3612",
        "Nome": "Cândido Faísca",
        "Curso": "Teatro",
        "Notas_sum": 39
    },
    {
        "Número": "7777",
        "Nome": "Cristiano Ronaldo",
        "Curso": "Desporto",
        "Notas_sum": 72
    },
    {
        "Número": "264",
        "Nome": "Marcelo Sousa",
        "Curso": "Ciência Política",
        "Notas_sum": 76
    }
]
```