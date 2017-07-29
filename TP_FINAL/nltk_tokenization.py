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

#~ import sys
#~ import re
#~ import os
#~ import nltk
#~ from nltk.tokenize import RegexpTokenizer
#~ from nltk import *


#~ f=open (os.path.join(os.getcwd(), 'Abstracts' , 'Todos_los_abstracts.txt'),'r')

#~ texto= f.read()

#~ texto = re.sub(r'[\]\[\(\)\{\}\<\>]', "", texto)


#~ tokens = nltk.word_tokenize(texto)

#~ nltk.concordance("ion")

#~ print tokens


##################33


# coding=utf-8


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.text import Text
import os
import re
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

def main():
    text = open(os.path.join(os.getcwd(), 'Abstracts' , 'Todos_los_abstracts.txt'),'r').read()
    text = re.sub(r'[\]\[\(\)\{\}\<\>]', "", text)
    tokens = word_tokenize(text)
    textList = Text(tokens)
    textList.dispersion_plot(["in", "ion", "Haberland", "cancer", "fibroblasts", 'molecule']) #Cada marca representa una instancia de esa palabra y cada fila cubre todo el texto. Hay un orden cronologico




if __name__ == '__main__':
    main()








           

   


	

