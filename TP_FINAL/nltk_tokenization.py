# coding=utf-8

#~ import nltk
#~ from nltk.tokenize import word_tokenize , sent_tokenize
#~ import sys
#~ import os

#~ reload(sys)  #Evita problemas con la codificación
#~ sys.setdefaultencoding('Cp1252')


            
#~ words_input_dir = os.path.join(os.getcwd(), 'Abstracts')

#~ for filename in os.listdir(words_input_dir):
    #~ if filename.endswith(".txt"):
        #~ with open(filename, "r") as input_file:
            #~ input_tokens = word_tokensize(input_file.read())


#~ import nltk

#~ import matplotlib

#~ import string


 	
#~ f=open('my-file.txt','r')
#~ texto= f.read()
#~ ##Aca le pondria algo que borre las lineas que arranquen con "<"
#~ texto = texto.translate(None, ['version','?']) #Borra la puntuacion, leer la documentacion de string
#~ tokens = nltk.word_tokenize(texto)


#~ print(tokens)    

#!/usr/bin/python

import re
import os

archivos = os.listdir(os.getcwd())

print archivos

for archivo in archivos:
	
	f=open(str(archivo),'r+')

	abstract = f.read()
	
	#~ print 'abstract editado : ', abstract 


	#~ # Delete Python-style comments

	abstract_editado = re.sub(r'(?m)^\<.*\n?', "", abstract)
	#~ print "abstract editado : ", abstract_editado

	f1 = open(archivo,'w+')
	f1.write(abstract_editado)







           

   


	

