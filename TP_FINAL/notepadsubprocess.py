#coding=utf-8

import subprocess
import sys

rango = 10 # La cantidad de partes en las que estara dividido el numero total.
total = int(sys.argv[1])
paso = int(total/rango)	
abstracts = [] 	
todos = []

def subproceso((inicio,fin)):
	
	for i in range(inicio,fin):
		p=subprocess.Popen(['python', 'script_prueba.py', str(i)])
		todos.append(p)

	exit_codes = [p.wait() for p in todos]
	

def Dividir_input(total,paso):
	for x in range(1,total,paso):
		abstracts.append((x,x+paso))
	return abstracts

abstracts = Dividir_input(total,paso) #Abstracts es una lista de tuplas de rango = paso.

	
if __name__== '__main__':
	
	for i in range(0,10):
		subproceso(abstracts[i])
		







