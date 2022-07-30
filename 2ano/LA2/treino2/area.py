'''

Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 

'''
# verífica se o valor está dentro do mapa
def verifica(mapa, i, j):
    return (i >= 0 and i< len(mapa)) and (j>=0 and j<len(mapa))


# depth first
def dfs(adj,o):
    return dfs_aux(adj,o,set(),{})

def dfs_aux(adj,o,vis,pai):
    vis.add(o)
    for d in adj[o]:
        if d not in vis:
            pai[d] = o
            dfs_aux(adj,d,vis,pai)
    return vis


#complexidade quadrática ://
# 100% 
def area(p,mapa):
    grafo = {}
    i=0
    
    #construir grafo
    while i < len(mapa):
        j = 0
        while j < len(mapa):
            grafo[(i,j)] = []
            # esquerda
            if(verifica(mapa, i, j-1) == True and mapa[i][j-1] == '.'):
                grafo[(i,j)].append( (i,j-1) )
            # direita
            if(verifica(mapa, i, j+1) == True and mapa[i][j+1] == '.'):
                grafo[(i,j)].append( (i,j+1) )
            # cima
            if(verifica(mapa, i-1, j) == True and mapa[i-1][j] == '.'):
                grafo[(i,j)].append( (i-1,j) )
            #baixo
            if(verifica(mapa, i+1, j) == True and mapa[i+1][j] == '.'):
                grafo[(i,j)].append( (i+1,j) )
            j+=1
        i+=1

    p = (p[1],p[0])
    vis = dfs(grafo, p)
    print(vis)
    
    
    return len(vis)