from math import prod
import re

def rangeToTuple(range):
    res = re.findall("(?:[0-9])+", range)
    nums = [int(num) for num in res]

    if len(nums) == 0:
        return [1, 1]
    if len(nums) == 1:
        return [1, nums[0]]
    return nums

aggregators = {
    "sum": sum,
    "media": lambda x : sum(x)/len(x),
    "prod": prod
}

with open("input.csv", "r") as f:
    lines = f.readlines()


headers = re.findall("([A-Za-z0-9úãóíáõé]+)+({(?:[0-9]+,?)+})?(::[A-Za-z]+)?", lines[0])
body = lines[1:] if len(lines) > 1 else []

cols = []
padding = 0
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

json = []
for row in body:
    res = re.split(",", re.sub("\n", "", row))
    ret = dict()

    for entry in cols:
        range = res[entry["start"]:entry["end"]]

        if len(range) > 1:
            converted = [int(n) for n in range if n != ""]
            if entry["aggregate_func"] == "":
                ret[entry["nome"]] = converted
            else:
                ret[f'{entry["nome"]}_{entry["aggregate_func"]}'] = aggregators[entry["aggregate_func"]](converted)
        else:
            ret[entry["nome"]] = range[0]
        
    json.append(ret)

with open("res.json", "w") as f:
    f.write(re.sub("'", '"', str(json)))

print(cols)


