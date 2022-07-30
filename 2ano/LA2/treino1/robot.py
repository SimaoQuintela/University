'''
Neste problema prentede-se que implemente uma função que calcula o rectângulo onde se movimenta um robot.

Inicialmente o robot encontra-se na posição (0,0) virado para cima e irá receber uma sequência de comandos numa string.
Existem quatro tipos de comandos que o robot reconhece:
  'A' - avançar na direcção para o qual está virado
  'E' - virar-se 90º para a esquerda
  'D' - virar-se 90º para a direita 
  'H' - parar e regressar à posição inicial virado para cima
  
Quando o robot recebe o comando 'H' devem ser guardadas as 4 coordenadas (minímo no eixo dos X, mínimo no eixo dos Y, máximo no eixo dos X, máximo no eixo dos Y) que definem o rectângulo 
onde se movimentou desde o início da sequência de comandos ou desde o último comando 'H'.

A função deve retornar a lista de todas os rectangulos (tuplos com 4 inteiros)
'''

def robot(comandos):
    movs = {
        0: (0,1),   # norte
        1: (1,0),   # este 
        2: (0,-1),  # sul
        3: (-1,0)   # oeste
    } 
    faced = 0
    mov = [0,0] # x,y
    maxX = 0
    maxY = 0
    minX = 0
    minY = 0
    r = []
    for com in comandos:
        if com == 'A':
            mov[0] += movs[faced][0]
            mov[1] += movs[faced][1]
            if(mov[0] > maxX):
                maxX = mov[0]
            elif(mov[0] < minX):
                minX = mov[0]
                
            if (mov[1] > maxY):
                maxY = mov[1]
            elif(mov[1] < minY):
                minY = mov[1]
        elif com == 'E':
            faced = (faced-1) % 4
        elif com == 'D':
            faced = (faced+1) % 4
        else:
            r.append((minX,minY,maxX,maxY))
            maxX = 0
            maxY = 0
            minX = 0
            minY = 0
            mov[0] = 0
            mov[1] = 0
            faced = 0
    
    return r
    