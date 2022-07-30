"""
Implemente uma função que, dada uma lista com registos de instantes de tempo e nome de piloto, 
descrevendo os tempos de passagem pela meta dos varios pilotos numa corrida de F1, 
devolva a lista com os nomes dos pilotos com a volta mais rápida ordenada por ordem alfabética. 
Assuma que todos os pilotos iniciaram a prova no instante 0.
"""

def minimo(corredores, corredor):
    
    min = corredores[corredor][0]
    
    r = corredores[corredor]
    
    for i in range(len(r)-1):
        if(corredores[corredor][i+1] - corredores[corredor][i] < min):
            print(corredores[corredor][i+1] - corredores[corredor][i])
            min = corredores[corredor][i+1] - corredores[corredor][i]
    
    
    
    return min

def minimo2(arrayDeMinimos):
    minimo = arrayDeMinimos[0]
    
    for x in arrayDeMinimos:
        if x < minimo:
            minimo = x
            
    return minimo

#100%        
#ew, so ugly. I'll think about a cleaner solution in the future
def formula1(log):
    log.sort(key = lambda x: (x[0]))
    if len(log) == 0:
        return []
    
    print(log)
    corredores = {}
    
    for lap in log:
        if lap[1] not in corredores:
            corredores[lap[1]] = [lap[0]]
        else:
            corredores[lap[1]].append(lap[0])

    voltaMinima = []
    for corredor in corredores:
        voltaMinima.append( (corredor, minimo(corredores, corredor)) )
    
    arrayDeMinimos = [x[1] for x in voltaMinima]
    minimaVolta = minimo2(arrayDeMinimos)
    
    result = []
    for x in voltaMinima:
        if(x[1] == minimaVolta):
            result.append(x[0])
    
    result.sort()
    
    
    return result
