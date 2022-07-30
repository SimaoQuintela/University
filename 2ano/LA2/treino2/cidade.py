'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que calcula o tamanho de uma cidade, 
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os 
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a 
letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.
'''

def dijkstra(adj,o):
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x:dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d[0] not in dist:
                orla.add(d[0])
                dist[d[0]] = float("inf")
            index = adj[v].index(d)
            if dist[v] + adj[v][index][1] < dist[d[0]]:
                dist[d[0]] = dist[v] + adj[v][index][1]
    return dist

 # 100%
def tamanho(ruas):
    cidade = {}
    
    for rua in ruas:
        if(rua[0] not in cidade):
            cidade[rua[0]] = []
        
        if(rua[-1] not in cidade):
            cidade[rua[-1]] = []
            
        if(rua[0] != rua[-1]):
            cidade[rua[0]].append( (rua[-1],len(rua)) )
            cidade[rua[-1]].append( (rua[0],len(rua)) )
        else:
            cidade[rua[0]].append( (rua[-1], len(rua)) )

    print(cidade)
        
    maxDist = 0
    for rua in cidade:
        maxD = max(filter(lambda x: x != float("inf"), dijkstra(cidade,rua).values()))
        print(maxD)
        if( maxD > maxDist):
            maxDist = maxD
    

    return maxDist