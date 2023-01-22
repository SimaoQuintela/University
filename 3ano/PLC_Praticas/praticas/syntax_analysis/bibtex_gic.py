import sys
import ply.yacc as yacc
from bibtex_lex import tokens

def p_grammar(p):
	"""                                      # z -> bibtex $ 
	bibtex : referencias                     #first(refs)=first(ref) {ID}

	referencias : referencias referencia     #first(ref) {ID}
	referencias :                            # follow(refs) { $ } U first(ref) { $,ID }

	referencia : ID '{' PAL ',' campos '}'   #{ ID }    
  
	campos : campos ',' campo                 # { PAL }
	campos : campo                            # { PAL }

	campo : PAL SEP  TEXTO                   #  { PAL }
	"""
	
#campos : campo outrosC  # { PAL }
#outrosC : ',' campos     # { , }            
#outrosC : €              # { '}' }


def p_error(p):
    print("Syntax error in input!",p)
    parser.success=False

parser = yacc.yacc()
parser.success=True

source = ""
for linha in sys.stdin:
	source += linha

parser.parse(source)
#print(source)
if parser.success:
   print('Parsing completed!')
else:
   print('Parsing failed!')

#result = parser.parse(source)
#print(result)

#f = open("bibtex.txt",encoding="utf-8")
#for linha in f:
#	source += linha

