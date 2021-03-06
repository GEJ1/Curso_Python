import sys
import re
import os
from sort_nicely import sort_nicely



def limpiar(directorio):
	
	todos_los_abstracts = open(os.path.join(os.getcwd(), 'Abstracts' , 'Todos_los_abstracts.txt'),'w+')	
	archivos = os.listdir(os.path.join(os.getcwd(), directorio))
	archivos = sort_nicely(archivos) #Ordena los archivos  que me da os.listdir
	
	for archivo in archivos:
		
		
		f = open(os.path.join(os.getcwd(), directorio , archivo),'r')

		abstract = f.read()
		
		abstract_editado = re.sub(r'(?m)^\<.*\n?', "", abstract) #Borra lo que aparece entre <> debido a venir de una pagina web
		abstract_editado2 = re.sub(r'\A1..', "", abstract_editado) # borra el "1. " con el que empiezan todos los abstracts
		abstract_editado3 = re.sub(r'[\[\]\(\)\{\}\<\>.\,\:\:\;]', "", abstract_editado2) #borra parentesis, corchetes, llaves y signos de puntuacion (Ej: .,:;)
		
		
		cada_abstract = open(os.path.join(os.getcwd(), directorio , archivo),'w+')
		
		cada_abstract.write(abstract_editado3)
		cada_abstract.close()
		todos_los_abstracts.write(abstract_editado3)
		
		
		
	todos_los_abstracts.close()

if __name__== '__main__':
	
	limpiar('Abstracts')
	

