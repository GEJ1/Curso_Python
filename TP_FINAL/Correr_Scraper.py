#coding=utf-8


import sys
import os
from scraper_library import Scraper, Scraper_pubmed

if __name__== '__main__':

	Scraper_pubmed1  = Scraper_pubmed()
	
	Scraper_pubmed1.crear_directorio()
	
	i = int(sys.argv[1])

	Scraper_pubmed1.Correr_Scraper(i)
	

	
	


		

	








	

