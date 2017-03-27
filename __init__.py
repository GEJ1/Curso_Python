from fama import famosos

famosos_numerados = [] #Nueva lista

i = 0 #Contador

for famoso in famosos:
	famosos_numerados.append(str(i + 1) + ' - ' + famoso)
	i = i + 1
	

print (famosos_numerados)
