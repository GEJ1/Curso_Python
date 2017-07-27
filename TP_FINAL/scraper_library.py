import requests
import os
import shutil


class Scraper(object):
	
	def __init__(self, directorio='',files_names='',base_url='',files_path=''):
		self.directorio = directorio
		self.files_path = files_path
		self.files_names = files_names
		self.base_url = base_url

	def crear_directorio(self):
		if not os.path.exists(self.directorio):
			os.makedirs(self.directorio)		

	def borrar_abstracts(self):
		shutil.rmtree(os.path.join(os.getcwd(), self.directorio))

	def Correr_Scraper(self, i):
		
		archivo = open(os.path.join(self.files_path ,self.files_names.format(str(i))) ,'w+') 
		toask =  self.base_url.format(str(i))
		print(i)
		page = requests.get(toask)

		archivo.write(page.content)
		
		
		
class Scraper_pubmed(Scraper):
	
	def __init__(self,**kwargs):
		Scraper.__init__(self)
		self.base_url = "https://www.ncbi.nlm.nih.gov/pubmed/{}?report=abstract&format=text"
		self.files_names = 'abstract_{}.txt'
		self.directorio = 'Abstracts'
		self.files_path = os.path.join(os.getcwd(), self.directorio)
		
	
		

