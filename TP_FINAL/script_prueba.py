#coding=utf-8

import requests
import sys

tupla = int(sys.argv[1])

Base_URL = "https://www.ncbi.nlm.nih.gov/pubmed/{}?report=abstract&format=text"

def busca_abstracts_pubmed(i):
	
	archivo = open('abstract'+ str(i) + '.txt' ,'w+') #Es necesario crear un archivo en el directorio que se llame "abstract.txt" (esto podría hacerse automaticamente)
	toask =  Base_URL.format(str(i))
	print(i)
	page = requests.get(toask)

	archivo.write(page.content)

	
	print "termine"
	
busca_abstracts_pubmed(tupla)




	

