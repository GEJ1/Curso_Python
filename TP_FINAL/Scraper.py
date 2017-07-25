#coding=utf-8

import requests
import sys
import os
import shutil
from time import time

class Scraper(object):
	
	def __init__(self, directorio):
		self.directorio = directorio

	def crear_directorio(self):
		if not os.path.exists(self.directorio):
			os.makedirs(self.directorio)		

	def borrar_abstracts(self):
		shutil.rmtree(os.path.join(os.getcwd(), self.directorio))

	def Correr_Scraper(self, i):
	
		archivo = open(os.path.join(abstr_path ,abstr_names.format(str(i))) ,'w+') 
		toask =  Base_URL.format(str(i))
		print(i)
		page = requests.get(toask)

		archivo.write(page.content)


	
	

if __name__== '__main__':

	Base_URL = "https://www.ncbi.nlm.nih.gov/pubmed/{}?report=abstract&format=text"

	abstr_names = 'abstract{}.txt'
	
	Scraper_pubmed  = Scraper('Abstracts')
	
	Scraper_pubmed.crear_directorio()

	abstr_path = os.path.join(os.getcwd(), 'Abstracts')

	i = int(sys.argv[1])
	
	

	Scraper_pubmed.Correr_Scraper(i)
	

	
	


		

	








	

