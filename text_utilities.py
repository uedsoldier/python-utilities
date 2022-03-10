from termcolor import colored
from num2words import num2words
from decimal import Decimal

def getQuantity_string(number, lang):
    numero_decimal = Decimal(number)
    print('Decimal: '+str(numero_decimal))
    entero = int(number)
    print('Integer: '+str(entero))
    fraccion =  int(round((numero_decimal % 1)*100,0))
    print('Fraction: {:.0f}'.format(fraccion))
    try:
        return num2words(entero, lang=lang), fraccion
    except NotImplementedError:
        print('Language {} not implemented'.format(lang))
        return num2words(entero, lang='es'), fraccion


def read_txtLines(file):
	try:
		with open(file,'r') as textfile:
			lines = textfile.readlines()
			return lines
	except Exception as e:
		print(colored(e,'red')) 
		raise SystemExit