import sys
import re
import os

def limpiar(directorio):
	
	for archivo in os.listdir(os.path.join(os.getcwd(), directorio)):
		
		f=open(os.path.join(os.getcwd(), directorio , archivo),'r')

		abstract = f.read()
		
		abstract_editado = re.sub(r'(?m)^\<.*\n?', "", abstract)
		abstract_editado2 = re.sub(r'\A1..', "", abstract_editado)
		
		f1 = open(os.path.join(os.getcwd(), directorio , archivo),'w+')
		
		f1.write(abstract_editado2)

if __name__== '__main__':
	
	limpiar('Abstracts')

