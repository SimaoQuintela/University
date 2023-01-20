
import sys
import re

semaforo = False
soma = 0

for linha in sys.stdin:
    if res := re.findall(r'(\d+)', linha):
        if(semaforo):
            for num in res:
                soma = soma + int(num)
    elif (re.search(r'on', linha, flags = re.IGNORECASE)):
        semaforo = True
        print("On again...")
    elif (re.search(r'off', linha, flags = re.IGNORECASE)):
        semaforo = False
        print("Off...")
    elif (re.search(r'=', linha)):
        print("Soma = ", soma)
    
print("A soma calculada final e: ", soma)
