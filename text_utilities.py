from termcolor import colored
from num2words import num2words
from decimal import Decimal

def getQuantity_string(number: int|float, lang: str) -> dict[str,int]:
    retVal = {
        'quantityString': '',
        'fraction': 0
    }
    decimal_number = Decimal(number)
    integer = int(number)
    fraction: int =  int(round((decimal_number % 1)*100,0))
    retVal['fraction']=fraction
    try:
        
        retVal['quantityString']= num2words(integer, lang=lang)
    except NotImplementedError:
        print('Language {} not implemented'.format(lang))
        retVal['quantityString']= num2words(integer, lang='es-MX')
    finally:
        return retVal

def read_txtLines(file):
	try:
		with open(file,'r') as textfile:
			lines = textfile.read().splitlines()
			return lines
	except Exception as e:
		print(colored(e,'red')) 
		raise SystemExit

if __name__ == '__main__':
    import sys
    try:
        qty = float(sys.argv[1])
        print(getQuantity_string(qty,'es-MX')['quantityString'])
    except Exception as e:
        print(e)    