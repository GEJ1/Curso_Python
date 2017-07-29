import sys
import re
import os
from sort_nicely import sort_nicely



def limpiar(directorio):
	
	f2 = open(os.path.join(os.getcwd(), 'Abstracts' , 'Todos_los_abstracts.txt'),'w+')	
	archivos = os.listdir(os.path.join(os.getcwd(), directorio))
	archivos = sort_nicely(archivos) #Ordena los archivos  que me da os.listdir
	
	for archivo in archivos:
		
		
		
		f=open(os.path.join(os.getcwd(), directorio , archivo),'r')

		abstract = f.read()
		
		abstract_editado = re.sub(r'(?m)^\<.*\n?', "", abstract)
		abstract_editado2 = re.sub(r'\A1..', "", abstract_editado)
		
		f1 = open(os.path.join(os.getcwd(), directorio , archivo),'w+')
		
		f1.write(abstract_editado2)
		f1.close()
		f2.write(abstract_editado2)
	f2.close()

if __name__== '__main__':
	
	limpiar('Abstracts')
	

