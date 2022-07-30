'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''

def frequencia(texto):
    words = texto.split()
    dic = {}
    
    for word in words:
        if word not in dic:
            dic[word] = 0
        dic[word] += 1
    
    words = set(words)
    words = list(words)
    words.sort(key=lambda x: (-dic[x], x) )

    return words