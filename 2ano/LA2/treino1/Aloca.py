"""
Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.
"""

def aloca(prefs):
    projects = {}
    nonAlocatedStudents = []
    
    "loop through students"
    for student in sorted(prefs):
        "check the projects already taken"
        projectsAlocated = projects.values()
        "loop through the project preference of the student"
        for project in prefs[student]:
            "if the project isn't already taken, add it"
            if project not in projectsAlocated and student not in projects:
                projects[student] = project
        "if all projects are already taken add it to the nonAlocatedStudents array"
        if student not in projects:
            nonAlocatedStudents.append(student)
    

    return nonAlocatedStudents        
