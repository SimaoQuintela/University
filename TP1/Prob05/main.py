import csv
import re
from json_write import write_on_json_file

lines = []
with open('./examples/alunos.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
    for row in spamreader:
        lines.append(row[0])

line_with_header = lines[0]
lines.pop(0)


headers = re.findall("([A-Za-z0-9úãóíáõé]+)+({((?:[0-9]+,?)+)})?", line_with_header)
json_headers = {}
i = 0
print(headers)
for header in headers:
    if "{" in header[1] and "}" in header[1]:
        min_max_array = re.split(",", header[2])
        if len(min_max_array) == 2:
            min_array = int(min_max_array[0])
            max_array = int(min_max_array[1])
        else:
            min_array = 1
            max_array = int(min_max_array[0])
        json_headers[i] = {}
        json_headers[i][header[0]+header[1]] = (min_array,max_array)  
         
    else:
        json_headers[i] = header[0]
    i+=1

print(json_headers)

#print(headers)
json_file_name = input("Nome do ficheiro JSON sem terminação: ") + ".json"
f = open(json_file_name, "w")
f.write("[\n")
f.close()
for (i,line) in enumerate(lines):
    f = open(json_file_name, "a")
    write_on_json_file(line, json_headers, f)
    if i != len(lines)-1:
        f.write("    },\n")
    else:
        f.write("    }")

f = open(json_file_name, "a")
f.write("\n]")
f.close()