from main import lines, re

name_frequency = {}
lines = [
        "575::1894-11-08::Aarao Pereira Silva::Antonio Pereira Silva::Francisca Campos Silva::",
        "887::1730-03-06::Joao Oliveira Magalhaes::Domingos Oliveira::Luisa Oliveira::Jose Oliveira Magalhaes,Irmao. Proc.21311.::",
        "853::1714-01-21::Joao Pacheco Andrade::Agostinho Pacheco Andrade::Catarina Leite Pereira::Joao Pacheco Leite,Sobrinho Materno. Proc.21010.::",
        "880::1727-08-22::Joao Paulo Araujo::Joao Goncalves Araujo::Maria Araujo Guimaraes::Bento Araujo Guimaraes,Irmao. Proc.20053.   Jeronimo Basilio Conceicao,Irmao. Proc.19709.  Manuel Araujo,Irmao. Proc.16025.::"
]

date = re.search(r'([0-9]{4}\-[0-9]{2}\-[0-9]{2})' ,lines[0])
print(date.group(0))

# Caso 1 - ::nome::nome::nome::
# :([A-Za-z| ]+):     - coloca nos grupos de índice ímpar o nome da pessoa

# Caso 2 - nome, relação parentesco, Proc.x
# ([A-Z][A-Za-z ]+),([A-Za-z ]+). ?(?i:(Proc.[0-9]+))
# grupo 0 - nome da pessoa
# grupo 1 - relação de parentesco
# grupo 2 - número de processo



# (([A-Za-z][A-Za-z| ]+),)+  -> pega nos casos    ::nome,       e      nome,    - dar split na vírgula e tenho os nomes

'''
for line in lines:
    
    names_and_year = re.search(r'([0-9]{4}\-[0-9]{2}\-[0-9]{2})([:]{2}[A-Za-z | ]+)+' ,line)
    if names_and_year != None:    
        print(names_and_year.group(0))
'''
    
    
