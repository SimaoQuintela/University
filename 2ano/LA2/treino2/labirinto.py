'''

Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista 
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.

'''

# verífica se o valor está dentro do mapa
def verifica(mapa, i, j):
    return (i >= 0 and i< len(mapa)) and (j>=0 and j<len(mapa))

def bfs(adj,o):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return pai

def caminhoMaisCurto(adj,o,d):
    pai = bfs(adj,o)
    caminho = [d]
    while d in pai:
        d = pai[d]
        caminho.insert(0,d)
    return caminho


def converteParaCoordenadas(caminho):
    r = ""
    for i in range(len(caminho) -1):
        par = (caminho[i+1][0] - caminho[i][0], caminho[i+1][1] - caminho[i][1])
        if(par[0] == 0 and par[1] == 1):
            r += "E"
        elif(par[0] == 0 and par[1] == -1):
            r += "O"
        elif(par[0] == 1 and par[1] == 0):
            r += "S"
        else:
            r += "N"
    return r

# it can be cleaner
# 100%
def caminho(mapa):
    grafo = {}
    
    for i in range(len(mapa)):
        for j in range(len(mapa)):
            grafo[(j,i)] = []
            if(verifica(mapa, j-1, i) == True and mapa[j-1][i] == ' '):
                grafo[(j,i)].append( (j-1, i) )
                
            if(verifica(mapa, j+1, i) == True and mapa[j+1][i] == ' '):
                grafo[(j,i)].append( (j+1, i) )
                
            if(verifica(mapa, j, i-1) == True and mapa[j][i-1] == ' '):
                grafo[(j,i)].append( (j, i-1) )
                
            if(verifica(mapa, j, i+1) == True and mapa[j][i+1] == ' '):
                grafo[(j,i)].append( (j, i+1) )
    
    print(grafo)
    r = caminhoMaisCurto(grafo, (0,0), (len(mapa)-1 , len(mapa)-1) )
    r2 = converteParaCoordenadas(r)
    
    return r2