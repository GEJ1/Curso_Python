# coding=utf-8

import nltk
from nltk.tokenize import word_tokenize , sent_tokenize
import sys
import os

reload(sys)  #Evita problemas con la codificación
sys.setdefaultencoding('Cp1252')


            
words_input_dir = os.path.join(os.getcwd(), 'Abstracts')

for filename in os.listdir(words_input_dir):
    if filename.endswith(".txt"):
        with open(filename, "r") as input_file:
            input_tokens = word_tokensize(input_file.read())
            


           

   


	

