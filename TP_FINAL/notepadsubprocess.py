import subprocess

#subprocess.call(['python', 'script_prueba.py'])
#subprocess.call(['python', 'script_prueba.py'])
#subprocess.call(['python', 'script_prueba.py'])
#subprocess.call(['python', 'script_prueba.py'])

todos = []
for i in range(1,100000):
	p=subprocess.Popen(['python','script_prueba.py', str(i)])
	todos.append(p)

exit_codes = [p.wait() for p in todos]



