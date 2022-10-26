import csv
import re

lines = []
with open('./examples/alunos.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        lines.append(row)

    
print(lines)

header = lines[0]
lines.pop(0)

print(header)
headers = {}
i = 0
for title in header:
    match = re.match(r"([A-Za-z]+)({([0-9]+,?[0-9]*)})", title)
    if match:
        groups = match.groups()

        headers[groups[0]] = {}


        for j in range(int(groups[-1])):
            index = groups[0] + f"[{j}]"
            headers[groups[0]][index] = i
            i+=1

        print(match.groups())

    else:
        headers[i] = title
        i+=1
print(headers)