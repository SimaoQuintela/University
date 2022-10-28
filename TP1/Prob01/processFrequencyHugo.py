from main import lines, re

f#requency = {}
years = {}

for line in lines:
    process_and_date = re.search('([0-9]+)[:]{2}([0-9]{4}\-[0-9]{2}\-[0-9]{2})', line)
    

    if process_and_date != None:
        process = process_and_date.group(1)
        date = process_and_date.group(2)
        data_splitted = re.split(r'-', date)
        year = data_splitted[0]

        
        if year not in years:
            years[year] = {}


        if process not in years[year]:
            years[year][process] = 0


        #if year not in frequency:
         #   frequency[year] = 1

        
        years[year][process] += 1
        #frequency[year] += 1
'''
suma = 0
for freq in frequency:
    suma += frequency[freq]

print(frequency)
print(suma)

'''

for year in years:
    print(f'Ano {year}:')
    for process in years[year]:
        print(f'Processo {process}:')
        print(f'Frequência: {years[year][process]}')
        print('\n')
    print('\n\n')
