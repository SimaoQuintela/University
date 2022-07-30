'''

O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.

'''
def removePaisesVis(visitados, paises):
    r = []
    for pais in paises:
        if pais not in visitados:
            r.append(pais)
            
    return r

# depth first
def dfs(adj,o):
    return dfs_aux(adj,o,set())

def dfs_aux(adj,o,vis):
    vis.add(o)
    for d in adj[o]:
        if d not in vis:
            dfs_aux(adj,d,vis)
    return vis


#complexidade quadrática na construção do grafo,
#no entanto a parte da travessia está bastante otimizada, só faço 1 travessia por componente
# 100%
def maior(vizinhos):
    if(vizinhos == []):
        return 0
    
    paises = []
    for i in vizinhos:
        for j in i:
            if j not in paises:
                paises.append(j)
    
    mapa = {}
    #construção do grafo
    i=0
    while i < len(vizinhos):
        # caso em que se trata de uma ilha, ou seja, não tem fronteiras
        if(len(vizinhos[i]) == 1):
            mapa[vizinhos[i][0]] = []
        j = 0
        while j < len(vizinhos[i])-1:
            if(vizinhos[i][j] not in mapa):
                mapa[vizinhos[i][j]] = []
            
            if(vizinhos[i][j+1] not in mapa):
                mapa[vizinhos[i][j+1]] = []
            
            if(vizinhos[i][j+1] not in mapa[vizinhos[i][j]]):
                mapa[vizinhos[i][j]].append(vizinhos[i][j+1])
            
            if(vizinhos[i][j] not in mapa[vizinhos[i][j+1]]):
                mapa[vizinhos[i][j+1]].append(vizinhos[i][j])
            
            j+=1
        i+=1
     
    # travessias pelas diferentes componentes
    maior = 1
    for pais in mapa:
        if(pais in paises):
            vis = dfs(mapa, pais)
            if(len(vis) > maior):
                maior = len(vis)
            # removo os países visitados pq fazem parte da mesma componente/continente
            paises = removePaisesVis(vis, paises)
    
    return maior


