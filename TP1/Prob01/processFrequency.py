from main import lines, re

frequency = {}
years = {}

for line in lines:
    process_and_date = re.search('([0-9]+)[:]{2}([0-9]{4}\-[0-9]{2}\-[0-9]{2})', line)
    
    if process_and_date != None:
        process = process_and_date.group(1)
        date = process_and_date.group(2)
        year = re.split(r'-', date)[0]
        years[year] = {}

        if year not in frequency:
            frequency[year] = 0

        
        years[year][process] = 1
        frequency[year] += 1

suma = 0
for freq in frequency:
    suma += frequency[freq]

print(frequency)
print(suma)
