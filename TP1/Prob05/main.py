import re

with open("input.txt", "r") as f:
    lines = f.readlines()

headers = lines[0]
body = lines[1:] if len(lines) > 1 else []



