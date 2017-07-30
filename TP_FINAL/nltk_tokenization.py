# coding=utf-8


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.text import Text
from nltk import FreqDist
from nltk.corpus import stopwords

import os
import re
import sys  
import string 


if __name__== '__main__':
	
	reload(sys)  
	sys.setdefaultencoding('utf8') #Necesario para el encoding

	text = open(os.path.join(os.getcwd(), 'Abstracts' , 'Todos_los_abstracts.txt'),'r').read()

	#Tokeniza el texto
	tokens = word_tokenize(text)

	filtered_words = [w for w in tokens if not w in stopwords.words('english')]

	 
	palabras_clave = []

	input_usuario = raw_input('Seleccione la opcion deseada: 1- Grafico de frecuencia  2- Grafico de dispersion\n')

	if input_usuario == '1':
		
		fdist1 = FreqDist(filtered_words)
		
		fdist1.plot(30,cumulative=False)
		
	elif input_usuario == '2':
		
		input_usuario = raw_input('Ingrese todas las palabras que desee separadas por un espacio\n')
		
		tokens_input = word_tokenize(input_usuario)
		
		for palabra in tokens_input:
			
			palabras_clave.append(palabra)
			
		
		textList = Text(filtered_words)
		textList.dispersion_plot(palabras_clave)
   

   


	

