'''

Neste problema pertende-se calcular quais os vértices centrais
de um grafo pesado não orientado.

A excentricidade de um vértice é a distância desse vértice
ao vértice mais afastado. Os vértices centrais (ou centros) de
um grafo são os que tem excentricidade mínima.

Os vértices do grado são identificados por letras do alfabeto.
O grafo será descrito através de uma sequência de arestas. Cada
aresta é descrita por uma string onde o primeiro e último caracteres
identificam os vértices adjacentes e os digitos no meio o peso da 
respectiva aresta.

A função deverá devolver a lista com todos os centros ordenados
alfabeticamente.

Se o grafo não for ligado deve devolver None.

'''
def fw(adj):
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
    return dist

def centros(arestas):
    grafo = {}
    if arestas == []:
        return []
    
    for aresta in arestas:
        if aresta[0] not in grafo:
            grafo[aresta[0]] = {}
        
        if aresta[-1] not in grafo:
            grafo[aresta[-1]] = {}
        
        peso = int(aresta[1:-1])
        grafo[aresta[0]][aresta[-1]] = peso
        grafo[aresta[-1]][aresta[0]] = peso
    print(grafo)
    
    distancias = {}
    dists = fw(grafo)
    
    print(dists)
    
    dists_aux = {}
    for vertice in dists:
        if(max(list(dists[vertice].values())) == float('inf')):
            return None
        dists_aux[vertice] = list(dists[vertice].values())
    
    mins = []
    for vertice in dists_aux:
        mins.append( (vertice, max(dists_aux[vertice])) )

    minimo = mins[0][1]
    for item in mins:
        if item[1] < minimo:
            minimo = item[1]

    r = []
    for item in mins:
        if item[1] == minimo:
            r.append(item[0])
    
    r.sort()
    
    return r