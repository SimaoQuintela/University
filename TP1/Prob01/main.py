# -- Problema: Alien username
import re 

f = open("processos.txt", "r")

lines = f.readlines()

  
# alínea a)
def processFrequency():
    years = {}

    for line in lines:
        process_and_date = re.search('([0-9]+)[:]{2}([0-9]{4}\-[0-9]{2}\-[0-9]{2})', line)
    

        if process_and_date != None:
            process = process_and_date.group(1)
            date = process_and_date.group(2)
            data_splitted = re.split(r'-', date)
            year = data_splitted[0]

        
            if year not in years:
                years[year] = 1
            else:
                years[year] += 1

    return years

# alínea b)
def year_to_century(year):
    return -(-year // 100)

def nameFrequency():
# centurys = {19: {"First": {"Ana": 10, "Joana": 40},
#                  "Last":  {"Quintela": 5, "Silva: 2000"}
#                  }
#            }
    centurys = {}
    for line in lines:
        date = re.search(r'([0-9]{4})\-([0-9]{2})\-([0-9]{2})' ,line)
        names_in_dots = re.findall(':([A-Za-z| ]+)(:)', line)
        names_with_procs = re.findall('([A-Z][A-Za-z ]+),([A-Za-z ]+). ?(?i:(Proc.[0-9]+))', line)
 
        names = names_in_dots + names_with_procs
    
        if date:
            year = int(date.group(1))
            century = year_to_century(year)
            if century not in centurys:
                centurys[century] = {}
                centurys[century]["First"] = {}
                centurys[century]["Last"] = {}

        for name in names:
            person_name = name[0] 
            name_splitted = re.split(" ", person_name)
            first_name = name_splitted[0]
            last_name = name_splitted[-1]
            if first_name not in centurys[century]["First"]:
                centurys[century]["First"][first_name] = 1
            else:
                centurys[century]["First"][first_name] += 1

            if last_name not in centurys[century]["Last"]:
                centurys[century]["Last"][last_name] = 1
            else:
                centurys[century]["Last"][last_name] += 1
    return centurys

# alínea c)
def relationFrequency():
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

    return rel_freq
    

# alínea d)
def info_to_json():
    json_info = {}

    valid_lines = 0
    i = 0
    while valid_lines < 20:
        line = lines[i]

        if line != '':
            process_and_date = re.search('([0-9]+)[:]{2}([0-9]{4}\-[0-9]{2}\-[0-9]{2})', line)
            both = process_and_date.group(0)

            # use the begining of the line as a key to make sure that we are not saving repeated info
            if both not in json_info:
                process = process_and_date.group(1)
                date = process_and_date.group(2)
            
            
                json_info[both] = {"Processo": process, "Data": date}

                # get son and parents and store person name as a value and parents names as a list of names 
                son_and_parents = re.findall(':([A-Za-z| ]+)(:)', line)

                # son_and_parents = [("Son name"), ("Parent name")* ]
                json_info[both]["Pessoa processada"] = son_and_parents[0][0]

                if len(son_and_parents) == 2:
                    json_info[both]["Mãe"] = son_and_parents[1][0]
                else:
                    json_info[both]["Pai"] = son_and_parents[1][0]
                    json_info[both]["Mãe"] = son_and_parents[2][0]

                # get the relations
                relations = re.findall('([A-Z][A-Za-z ]+),([A-Za-z ]+). ?(?i:(Proc.[0-9]+))', line)
                if relations:
                    # relation = ("Person name", "Relation designation")
                    for relation in relations:
                        json_info[both][relation[1]] = relation[0]


                valid_lines+=1
    
        i+=1
    return json_info

def write_on_json():
    json_info = info_to_json()    
    f = open('res.json', 'w')

    f.write('[\n')


    for (i,entry) in enumerate(json_info):
        f.write('   {\n')
        data = json_info[entry]
        for (j, key) in enumerate(data):
            f.write(f'       \"{key}\": \"{data[key]}\"')

            if j == len(data)-1:
                f.write('\n')
            else:
                f.write(',\n')
            

        if i == len(json_info)-1:
            f.write('   }\n')
        else:
            f.write('   },\n')

    f.write(']\n')
    f.close()



# Menu de visualização de resultados
choose = input("Escolha um número:\n1-Frequência de Processos\n2-Frequência de nomes por século\n3-Frequência de relações\n4-Escrever num json\n5-Sair\nOpção: ")
while(choose != '5'):

    if choose == '1':
        year = str(input("Insira o ano(0 - print a tudo): "))
        proc_freq = processFrequency()
        if year != '0':
            print(proc_freq[year])
        else:
            print(processFrequency())
    elif choose == '2':
        century = int(input('Século(0 - print a tudo): '))
        name_freq = nameFrequency()
        if century != '0':
            print(name_freq[century])
        else:
            print(name_freq)
        
    elif choose == '3':
        rels = relationFrequency()
        relation = str(input('Relação(0 - print a tudo): '))
        if relation != '0':
            print(rels[relation])
        else:
            print(rels)
    else:
        write_on_json()

    choose = input("Escolha um número:\n1-Frequência de Processos\n2-Frequência de nomes por século\n3-Frequência de relações\n4-Escrever num json\n5-Sair\nOpção: ")
