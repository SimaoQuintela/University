# Relatório

## Enunciado
Pretende-se fazer um programa em Python que converta um ficheiro CSV (Comma separated values) para o formato JSON.

## Resolução
Na seguinte secção vamos apresentar a resolução do problema. A apresentação está estruturada da seguinte forma:

- Estrutura do programa
- Estruturas de dados
- Processamento dos cabeçalhos
- Processamento das linhas do ficheiro
- Escrita do resultado em formato JSON

### Estrutura do Programa
Após analisar o problema e exemplos fornecidos pelo professor, decidímos criar este conversor da seguinte forma.  
Primeiramente vai ser lido o ficheiro, depois vão ser processados os cabeçalhos através da criação de uma estrutura  
em código que espelha a estrutura do ficheiro. De seguida, a estrutura referida anteriormente vai utilizada para processar  
as linhas do ficheiro, transformando-as e guardando-as num array. Para finalizar esse array é convertido em texto no formato  
JSON.

### Estruturas de dados
As estruturas de dados são *array* de cabeçalhos, *array* de linhas e um dicionário funções agregadoras.  
O array de cabeçalhos é um array de dicionários que vai guardar toda a informação dos cabeçalhos do  
ficheiro CSV e organiza-la da seguinte forma.
```py
    {
        "nome":  # nome do campo do csv
        "min":   # comprimento minimo do campo caso seja uma lista
        "start": # indice inicial
        "end":   # indice final
        "aggregate_func": # nome da função a executar para agregar a lista
    }
```

O array de linhas é um array de dicionários também, mas estes têm a estrura da linha com a chave a ser um cabeçalho  
e o valor a ser a informação desse cabeçalho já processada.  
```py
    {
        "Número": "264",
        "Nome": "Marcelo Sousa",
        "Curso": "Ciência Política",
        "Notas_media": 19.0,
        "Soma_prod": 2496
    }
```

O dicionário de funções agregadoras contém entradas em que a chave é o nome da função e o valor é a função em si.
```py
    {
        "sum": sum,
        "media": lambda x : sum(x)/len(x),
        "prod": prod
    }
```


### Processamento dos cabeçalhos
Para processar os cabeçalhos executamos um *findall* que nos permite tornar a linha num array de tuplos  
que tem a seguinte forma (nome, intervalo de colunas, função agregadora). De seguida percorremos esse  
array e convertemo-lo na primeira estrutura mencionada anteriormente.
```py
def rangeToTuple(range):
    res = re.findall("(?:[0-9])+", range)
    nums = [int(num) for num in res]

    if len(nums) == 0:
        return [1, 1]
    if len(nums) == 1:
        return [1, nums[0]]
    return nums

headers = re.findall("([A-Za-z0-9úãóíáõé]+)+({(?:[0-9]+,?)+})?(::[A-Za-z]+)?", lines[0])

# Build column structure in dictionaries
padding = 0
cols = []

for i, (nome, range, func) in enumerate(headers):
    min, max = rangeToTuple(range)
    entry = {
        "nome":  nome,
        "min":   min,
        "start": padding+i,
        "end":   padding+i+max,
        "aggregate_func": func[2:]
    }
    padding += max - 1
    cols.append(entry)
```

### Processamento das linhas do ficheiro
Para processar as linhas utilizamos a estrutura criada anteriormente, verifica-mos que tipo de transformações  
têm de ser efectuadas para cada conjunto de colunas e preenchemos o dicionário com a informação de cada linha.  

```py
aggregators = {
    "sum": sum,
    "media": lambda x : sum(x)/len(x),
    "prod": prod
}

def rowToDict(row, cols):
    fields = re.split(",", re.sub("\n", "", row))
    dic = dict()

    for entry in cols:
        range = fields[entry["start"]:entry["end"]]

        if len(range) <= 1:
            dic[entry["nome"]] = range[0]
            continue

        converted = [int(n) for n in range if n != ""]
        if entry["aggregate_func"] == "":
            dic[entry["nome"]] = converted
        else:
            dic[f'{entry["nome"]}_{entry["aggregate_func"]}'] = aggregators[entry["aggregate_func"]](converted)

    return dic

body = lines[1:] if len(lines) > 1 else []

json = [rowToDict(row, cols) for row in body]
```

### Escrita do resultado em formato JSON
Na escrita do resultado temos tabulação parametrizável e aquilo que é feito é a conversão para texto,  
utilizando *fstrings* para converter cada par do dicionário num par de JSON e o dicionário em si num objecto  
depois todo esse texto é concatenado de forma a apresentar o resultado final correctamente.

```py
json = [rowToDict(row, cols) for row in body]

# Convert to JSON
tab = "    "

def renderPair(key, value):
    n_value = ('"' + value + '"') if type(value) is str else value
    return f'"{key}": {n_value}'

def renderObj(entry):
    outElem = f'{tab}{{\n{tab*2}'
    outElem += f',\n{tab*2}'.join([renderPair(key, value) for key, value in entry.items()])
    outElem += f'\n{tab}}}'
    return outElem

elems = [renderObj(entry) for entry in json]
out = "[\n" + ",\n".join(elems) + "\n]"


# Write result
with open("res.json", "w") as f:
    f.write(out)
```
