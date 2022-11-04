# 1. c)

from main import lines, re

# Caso 1 - ::nome::nome::nome::
# :([A-Za-z| ]+):     - coloca nos grupos de índice ímpar o nome da pessoa

# Caso 2 - nome, relação parentesco, Proc.x
# ([A-Z][A-Za-z ]+),([A-Za-z ]+). ?(?i:(Proc.[0-9]+))
# grupo 0 - nome da pessoa
# grupo 1 - relação de parentesco
# grupo 2 - número de processo

rel_freq = {}
rel_freq["Progenitores"] = 0
rel_freq["Filho"] = 0

for line in lines:
    parents_and_son = re.findall(":([A-Za-z| ]+):", line)
    
    if parents_and_son:
        parents = parents_and_son[1:]
        rel_freq["Filho"] += 1
        rel_freq["Progenitores"] += len(parents)

    relations = re.findall("([A-Z][A-Za-z ]+),([A-Za-z ]+). ?(?i:(Proc.[0-9]+))", line)
    if relations:
        for relation in relations:
            if relation[1] not in rel_freq:
                rel_freq[relation[1]] = 1
            else:
                rel_freq[relation[1]] += 1

print(rel_freq)
