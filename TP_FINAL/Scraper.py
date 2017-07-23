#coding=utf-8

import requests
import sys
import os

def crear_directorio(directorio):
	if not os.path.exists(directorio):
		os.makedirs(directorio)

def Scraper(i):
	
	archivo = open(os.path.join(abstr_path ,abstr_names.format(str(i))) ,'w+') 
	toask =  Base_URL.format(str(i))
	print(i)
	page = requests.get(toask)

	archivo.write(page.content)

	
	print "termine"
	

if __name__== '__main__':

	Base_URL = "https://www.ncbi.nlm.nih.gov/pubmed/{}?report=abstract&format=text"
	
	abstr_names = 'abstract{}.txt'

	crear_directorio('Abstracts')

	abstr_path = os.path.join(os.getcwd(), 'Abstracts')

	i = int(sys.argv[1])

	Scraper(i)






	

