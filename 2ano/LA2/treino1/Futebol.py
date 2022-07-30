'''
Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com 
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.
'''

def tabela(jogos):
    tabClass= {} # {equipa: [pontos,golos]}  exemplo: {Benfica: [10,5], Porto: [0,-10], Gil Vicente: [9, 4]}
        
    for jogo in jogos:
        if jogo[0] not in tabClass:
            tabClass[jogo[0]] = [0,0]
        if jogo[2] not in tabClass:
            tabClass[jogo[2]] = [0,0]
        
        difGolos = jogo[1] - jogo[3]
        if(jogo[1] > jogo[3]):
            tabClass[jogo[0]][0] += 3
            tabClass[jogo[0]][1] += difGolos
            tabClass[jogo[2]][1] -= difGolos
        elif(jogo[1] < jogo[3]):
            tabClass[jogo[2]][0] += 3
            tabClass[jogo[2]][1] += difGolos
            tabClass[jogo[0]][1] -= difGolos
        else:
            tabClass[jogo[0]][0] += 1
            tabClass[jogo[2]][0] += 1
            
    "r = (equipa, pontos, difGolos)"
    r = [(equipa, tabClass[equipa][0], tabClass[equipa][1]) for equipa in tabClass]
    r.sort(key=lambda x: (-tabClass[x[0]][0], -tabClass[x[0]][1], x) )
    result = [(equipa[0], equipa[1]) for equipa in r]
    
    return result