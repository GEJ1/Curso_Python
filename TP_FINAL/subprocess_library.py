import subprocess



def subproceso((inicio,fin)):
	todos = []
	
	for i in range(inicio,fin):
		p=subprocess.Popen(['python', 'Correr_Scraper.py', str(i)])
		todos.append(p)

	exit_codes = [p.wait() for p in todos]
	

def dividir_input(total,paso):
	archivos = [] 	
	for x in range(1,total,paso):
		archivos.append((x,x+paso))
	return archivos
