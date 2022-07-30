"""
Um hacker teve acesso a um log de transações com cartões de
crédito. O log é uma lista de tuplos, cada um com os dados de uma transação,
nomedamente o cartão que foi usado, podendo alguns dos números estar
ocultados com um *, e o email do dono do cartão.

Pretende-se que implemente uma função que ajude o hacker a 
reconstruir os cartões de crédito, combinando os números que estão
visíveis em diferentes transações. Caso haja uma contradição nos números 
visíveis deve ser dada prioridade à transção mais recente, i.é, a que
aparece mais tarde no log.

A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de igualdade
neste critério, aos emails menores (em ordem lexicográfica).
"""

def hacker(log):
    operacoes = {}
    for operacao in log:
        if(operacao[1] not in operacoes):
            operacoes[operacao[1]] = [operacao[0]]
        else:
            operacoes[operacao[1]].append(operacao[0])
    
    cartoes = []
    for cartao in operacoes:
        codigo = list(operacoes[cartao][0])
        for numero in operacoes[cartao]:
            for i in range(16): #trigger no range(16)
                if(numero[i] != '*'):
                    codigo[i] = numero[i]
            

        cartoes.append(("".join(codigo), cartao))
    cartoes.sort(key= lambda x: ( x[0].count('*') , x[1]))
        

    return cartoes