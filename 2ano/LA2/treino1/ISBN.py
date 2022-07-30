'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos. 
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos, 
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
'''

def isbn(livros):
    flag1 = 1
    invalid = []

    for livro in livros.items():
        r = 0
        for number in livro[1][:-1]:
            if flag1 == 1:
                r += 1* int(number,10)
                flag1 = 0
            else:
                r += 3* int(number,10)
                flag1 = 1
            
        r += int(livro[1][-1],10)
                
        if(r % 10 != 0):
            invalid.append(livro[0])
            
    invalid.sort()
    return invalid
            