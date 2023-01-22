import re

data = '31/10/2021'

fraseFonte = input(">> ")
while fraseFonte != "":
   nova_data = re.sub(
	    r'([0-9]{1,2})/([0-9]{1,2})/([0-9]{4})',
	    r'\3/\2/\1',
	    fraseFonte)
   print(nova_data)
   fraseFonte = input(">> ")
