'''
Neste problema pretende-se que implemente uma função que calcula a distância
entre duas cidades num mapa.

O mapa é rectangular e definido por uma lista de strings de igual comprimento,
onde um caracter 'X' marca a existência de uma cidade e um '#' uma estrada.
Neste mapa só é possível viajar na horizontal ou na vertical. As cidades de
origem e destino são identificadas pelas respectivas coordenadas horizontal e
vertical, medidas a partir do canto superior esquerdo. Se as coordenadas destino
e origem não forem cidades a função deverá retornar None. Se não houver
caminho entre as duas cidades deverá retornar float("inf").

    mapa = ["#X###X",
            "#  #  ",
            "#X##  ",
            "     X",
            "  X###"]

        ("in: (1,0) (1,2)")
'''

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


def verifica(mapa,x,y):
    return (0 <= x < len(mapa[0])) and (0 <= y < len(mapa)) and (mapa[y][x] != " ")

def distancia(mapa,o,d):
    adj = {}

    if mapa[d[1]][d[0]] != 'X' or mapa[o[1]][o[0]] != 'X':
        return None

    for y in range(len(mapa)):
        for x in range(len(mapa[0])):
            if (x,y) not in adj:
                adj[(x,y)] = []

            if verifica(mapa,x+1,y) and mapa[y][x] != " ":
                adj[(x,y)].append((x+1,y))

            if verifica(mapa,x-1,y) and mapa[y][x] != " ":
                adj[(x,y)].append((x-1,y))

            if verifica(mapa,x,y+1) and mapa[y][x] != " ":
                adj[(x,y)].append((x,y+1))

            if verifica(mapa,x,y-1) and mapa[y][x] != " ":
                adj[(x,y)].append((x,y-1))

    print(adj)

    if d in adj:
        pai = bfs(adj,o)
        caminho = [d]
        while d in pai:
            d = pai[d]
            caminho.insert(0,d)
    else:
        return float("inf")

    print(caminho)

    if len(caminho) <= 2:
        return float("inf")

    return len(caminho)-1
