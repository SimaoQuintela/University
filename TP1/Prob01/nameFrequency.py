# 1. b)

from main import lines, re

def year_to_century(year):
    return -(-year // 100)


name_frequency = {}

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
        last_name = name_splitted[0]
        if first_name not in centurys[century]["First"]:
            centurys[century]["First"][first_name] = 1
        else:
            centurys[century]["First"][first_name] += 1

        if last_name not in centurys[century]["Last"]:
            centurys[century]["Last"][last_name] = 1
        else:
            centurys[century]["Last"][last_name] += 1
        
                
                


print(centurys[18])