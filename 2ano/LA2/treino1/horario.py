"""

Implemente uma função que calcula o horário de uma turma de alunos.
A função recebe dois dicionários, o primeiro associa a cada UC o
respectivo horário (um triplo com dia da semana, hora de início e
duração) e o segundo associa a cada aluno o conjunto das UCs em
que está inscrito. A função deve devolver uma lista com os alunos que
conseguem frequentar todas as UCs em que estão inscritos, indicando
para cada um desses alunos o respecto número e o número total de horas
semanais de aulas. Esta lista deve estar ordenada por ordem decrescente
de horas e, para horas idênticas, por ordem crescente de número.
"""

# function that checks if there's overlap between two different ucs
# It checks as well if the uc belongs to the ucs "list".
def overlap(aluno, alunos, ucs):
    
    for uc1 in alunos[aluno]:
        for uc2 in alunos[aluno]:
            # uc1 or uc2 not in the ucs dictionary
            if(uc1 not in ucs or uc2 not in ucs):
                return True
            else:
                startHourUc1 = ucs[uc1][1]
                endHourUc1 = startHourUc1 + ucs[uc1][2]
                startHourUc2 = ucs[uc2][1]
                endHourUc2 = startHourUc2 + ucs[uc2][2]
                #      different uc's    ----     on the same day      -------                overlapping
                if( (uc1 != uc2) and (ucs[uc1][0] == ucs[uc2][0]) and ((startHourUc1 <= startHourUc2 <= endHourUc1) or (startHourUc2 <= startHourUc1 <= endHourUc2)) ):
                    return True
                
    return False


def horario(ucs,alunos):
    
    okStudents = []
    for aluno in alunos:
        if(overlap(aluno, alunos, ucs) == False):
            okStudents.append(aluno)
            
    print(okStudents)
    hours = 0
    r = []
    for student in okStudents:
        for uc in alunos[student]:
            hours += ucs[uc][2]
        r.append((student, hours))
        hours = 0
    
    r.sort(key = lambda x: (-x[1], x[0]))
    

    return r