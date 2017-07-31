import sys
import os

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.text import Text
from nltk import FreqDist
from nltk.corpus import stopwords
import pickle

reload(sys)  
sys.setdefaultencoding('utf8') #Necesario para el encoding

text = open(os.path.join(os.getcwd(), 'Abstracts' , 'Todos_los_abstracts.txt'),'r').read()

#Tokeniza el texto
tokens = word_tokenize(text)

tokens_listos = [w for w in tokens if not w in stopwords.words('english')]


texto_tokenizado = open(os.path.join(os.getcwd(), 'Abstracts' , 'texto_tokenizado.txt'),'w+')


 

# this writes the object a to the
# file named 'testfile'
pickle.dump(tokens_listos,texto_tokenizado.txt)   

# here we close the fileObject
texto_tokenizado.close()
# we open the file for reading
#~ fileObject = open(file_Name,'r') 
