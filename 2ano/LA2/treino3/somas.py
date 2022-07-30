"""

Implemente uma função que calula qual a subsequência (contígua e não vazia) de 
uma sequência de inteiros (também não vazia) com a maior soma. A função deve 
devolver apenas o valor dessa maior soma.

Sugere-se que começe por implementar (usando recursividade) uma função que 
calcula o prefixo de uma sequência com a maior soma. Tendo essa função 
implementada, é relativamente adaptá-la para devolver também a maior soma de toda
a lista.

"""

def maxsoma(lista):
    maxSum = lista[0]
    cache = [maxSum]
    
    for i in range(1,len(lista)):
        cache.append(max(cache[i-1] + lista[i], lista[i]))
        maxSum = max(maxSum, cache[i])
        
    return maxSum
