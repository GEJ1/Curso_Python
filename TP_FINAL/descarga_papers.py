#coding=utf-8

import subprocess
import sys


rango = int(sys.argv[2])  # La cantidad de partes en las que estara dividido el numero total. Si no da un entero te descarga uno de menos.
total = int(sys.argv[1]) #Total a descargar
paso = int(total/rango)	
abstracts = [] 	
todos = []

def subproceso((inicio,fin)):
	
	for i in range(inicio,fin):
		p=subprocess.Popen(['python', 'Scraper.py', str(i)])
		todos.append(p)

	exit_codes = [p.wait() for p in todos]
	

def Dividir_input(total,paso):
	for x in range(1,total,paso):
		abstracts.append((x,x+paso))
	return abstracts



# poner en la consola python descarga_papers.py "Total de papers a descargar" "cantidad de procesos en paralelo"	

if __name__== '__main__':
	
	abstracts = Dividir_input(total,paso)
	
	for i in range(0,int(sys.argv[2])):
		subproceso(abstracts[i])
		







