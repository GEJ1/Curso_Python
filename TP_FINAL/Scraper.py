#coding=utf-8

import requests
import sys
import os
import shutil
from time import time


def crear_directorio(directorio):
	if not os.path.exists(directorio):
		os.makedirs(directorio)

def borrar_abstracts():
	shutil.rmtree(os.path.join(os.getcwd(), 'Abstracts'))

def Scraper(i):
	
	archivo = open(os.path.join(abstr_path ,abstr_names.format(str(i))) ,'w+') 
	toask =  Base_URL.format(str(i))
	print(i)
	page = requests.get(toask)

	archivo.write(page.content)

	
	print "termine"

	
	
tiempo_inicial = time()
if __name__== '__main__':

	Base_URL = "https://www.ncbi.nlm.nih.gov/pubmed/{}?report=abstract&format=text"

	abstr_names = 'abstract{}.txt'

	crear_directorio('Abstracts')

	abstr_path = os.path.join(os.getcwd(), 'Abstracts')

	i = int(sys.argv[1])
	
	

	Scraper(i)

tiempo_final = time()	
	
tiempo_ejecucion = tiempo_final - tiempo_inicial

print 'El tiempo de ejecucion fue:',tiempo_ejecucion 
		

	








	

