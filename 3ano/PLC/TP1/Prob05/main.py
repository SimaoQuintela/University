import re
import sys
from math import prod


# Read file
filename = sys.argv[1] if len(sys.argv) > 1 else "./examples/input.csv"
with open(filename, "r") as f:
    lines = f.readlines()

headers = re.findall("([A-Za-z0-9úãóíáõé]+)+({(?:[0-9]+,?)+})?(::[A-Za-z]+)?", lines[0])
body = lines[1:] if len(lines) > 1 else []


# Build column structure in dictionaries
padding = 0
cols = []

def rangeToTuple(range):
    res = re.findall("(?:[0-9])+", range)
    nums = [int(num) for num in res]

    if len(nums) == 0:
        return [1, 1]
    if len(nums) == 1:
        return [1, nums[0]]
    return nums

for i, (nome, range, func) in enumerate(headers):
    min, max = rangeToTuple(range)
    entry = {
        "nome":  nome,
        "min":   min,
        "start": padding+i,
        "end":   padding+i+max,
        "aggregate_func": func[2:]
    }
    padding += max - 1
    cols.append(entry)


# Build body structure in dictionaries
aggregators = {
    "sum": sum,
    "media": lambda x : sum(x)/len(x),
    "prod": prod
}

def rowToDict(row, cols):
    fields = re.split(",", re.sub("\n", "", row))
    dic = dict()

    for entry in cols:
        range = fields[entry["start"]:entry["end"]]

        if len(range) <= 1:
            dic[entry["nome"]] = range[0]
            continue

        converted = [int(n) for n in range if n != ""]
        if entry["aggregate_func"] == "":
            dic[entry["nome"]] = converted
        else:
            dic[f'{entry["nome"]}_{entry["aggregate_func"]}'] = aggregators[entry["aggregate_func"]](converted)

    return dic

json = [rowToDict(row, cols) for row in body]


# Convert to JSON
tab = "    "

def renderPair(key, value):
    n_value = ('"' + value + '"') if type(value) is str else value
    return f'"{key}": {n_value}'

def renderObj(entry):
    outElem = f'{tab}{{\n{tab*2}'
    outElem += f',\n{tab*2}'.join([renderPair(key, value) for key, value in entry.items()])
    outElem += f'\n{tab}}}'
    return outElem

elems = [renderObj(entry) for entry in json]
out = "[\n" + ",\n".join(elems) + "\n]"


# Write result
with open("res.json", "w") as f:
    f.write(out)
