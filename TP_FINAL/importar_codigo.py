import requests
import os
import shutil

class Scraper(object):
	
	def __init__(self, directorio):
		self.directorio = directorio
		self.abstr_path = os.path.join(os.getcwd(), 'Abstracts')
		self.abstr_names = 'abstract{}.txt'
		self.Base_URL = "https://www.ncbi.nlm.nih.gov/pubmed/{}?report=abstract&format=text"

	def crear_directorio(self):
		if not os.path.exists(self.directorio):
			os.makedirs(self.directorio)		

	def borrar_abstracts(self):
		shutil.rmtree(os.path.join(os.getcwd(), self.directorio))

	def Correr_Scraper(self, i):
		
		archivo = open(os.path.join(self.abstr_path ,self.abstr_names.format(str(i))) ,'w+') 
		toask =  self.Base_URL.format(str(i))
		print(i)
		page = requests.get(toask)

		archivo.write(page.content)
