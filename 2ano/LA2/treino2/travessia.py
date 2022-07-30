'''

Implemente uma função que calcula o menor custo de atravessar uma região de
Norte para Sul. O mapa da região é rectangular, dado por uma lista de strings,
onde cada digito representa a altura de cada ponto. Só é possível efectuar 
movimentos na horizontal ou na vertical, e só é possível passar de um ponto
para outro se a diferença de alturas for inferior ou igual a 2, sendo o custo 
desse movimento 1 mais a diferença de alturas. O ponto de partida (na linha
mais a Norte) e o ponto de chegada (na linha mais a Sul) não estão fixados à
partida, devendo a função devolver a coordenada horizontal do melhor
ponto para iniciar a travessia e o respectivo custo. No caso de haver dois pontos
com igual custo, deve devolver a coordenada mais a Oeste.

'''
def verifica(mapa, i, j):
    return (0<=i<len(mapa[0]) and 0<=j<len(mapa))

def dijkstra(adj,o):
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x: dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                dist[d] = dist[v] + adj[v][d]
                
    return dist


def travessia(mapa):
    grafo = {}
    
    for j in range(len(mapa)):
        for i in range(len(mapa[0])):
            if (i,j) not in grafo:
                grafo[(i,j)] = {}
            
            #esquerda
            if(verifica(mapa, i-1, j) == True and abs(int(mapa[j][i]) - int(mapa[j][i-1])) <= 2):
                grafo[(i,j)][(i-1,j)] = 1 + abs(int(mapa[j][i]) - int(mapa[j][i-1]))
            #direita
            if(verifica(mapa, i+1, j) == True and abs(int(mapa[j][i]) - int(mapa[j][i+1])) <= 2):
                grafo[(i,j)][(i+1,j)] = 1 + abs(int(mapa[j][i]) - int(mapa[j][i+1]))
            #cima
            if(verifica(mapa, i, j-1) == True and abs(int(mapa[j][i]) - int(mapa[j-1][i])) <= 2):
                grafo[(i,j)][(i,j-1)] = 1 + abs(int(mapa[j][i]) - int(mapa[j-1][i]))
            #baixo
            if(verifica(mapa, i, j+1) == True and abs(int(mapa[j][i]) - int(mapa[j+1][i])) <= 2):
                grafo[(i,j)][(i,j+1)] = 1 + abs(int(mapa[j][i]) - int(mapa[j+1][i]))
            
    print(grafo)
    
    r = (0,0)
    dists = []
   
    for k in range(len(mapa[0])):
        custos = dijkstra(grafo, (k,0))
        for i in range(len(mapa[0])):
            if (i, len(mapa)-1) in custos:
                dists.append( (k, custos[(i,len(mapa)-1)])  )
        
    
    dists.sort(key = lambda x: (x[1],x[0]))
    print(dists)


    
    return dists[0]


