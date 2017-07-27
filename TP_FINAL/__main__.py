#coding=utf-8


import sys
from time import time
from subprocess_library import subproceso , dividir_input


# poner en la consola python __main__.py "Total de papers a descargar" "cantidad de procesos en paralelo"

if __name__== '__main__':

	
	rango = int(sys.argv[2])  # La cantidad de partes en las que estara dividido el numero total. Si no da un entero te descarga uno de menos.
	total = int(sys.argv[1]) #Total a descargar
	paso = int(total/rango)	
	
	
	
	archivos = dividir_input(total,paso)	
		
	tiempo_inicial = time()
	
	for i in range(0,int(sys.argv[2])):
		subproceso(archivos[i])
		
	
	tiempo_final = time()
	
	
	tiempo_ejecucion = tiempo_final - tiempo_inicial
	
	print 'El tiempo de ejecucion fue:',tiempo_ejecucion 
	

	
		







