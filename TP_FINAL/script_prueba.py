# coding=utf-8

import requests
def busca_papers(a):
	
	file = open('testfile.txt','w') #Es necesario crear un archivo en el directorio que se llame "testfile.txt" (esto podría hacerse automaticamente)
	i = 1

	while i < a:
	
		page = requests.get("https://www.ncbi.nlm.nih.gov/pubmed/" + str(i) + "?report=abstract&format=text")

		file.write(page.content)
	
		i = i + 1
	
busca_papers(5)	
