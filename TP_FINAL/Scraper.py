#coding=utf-8

from importar_codigo import Scraper
import sys
import os

if __name__== '__main__':

	Scraper_pubmed  = Scraper('Abstracts')
	
	Scraper_pubmed.crear_directorio()
	
	i = int(sys.argv[1])

	Scraper_pubmed.Correr_Scraper(i)
	

	
	


		

	








	

