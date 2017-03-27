# coding=utf-8
'''#1.4 Comenzando a programar - Print, if, elif, else - tipos de datos

#Escribir un programa que diga "Aguante la Comic Sans" 

print('aguante la comic sans')


##################################################################################################################################


#Evaluar 4>3 and print("hola") - Explicar que sucede, generar un ejemplo donde la sentencia "hola" NO se ejecute.

if 4>3: #Con esa guarda el programa se ejecuta siempre debido a que siempre es True.
	print('hola')

if 3>4: #Aca la guarda es siempre False, por lo que no entra al print.
	print ('hola')

##################################################################################################################################

#Escribir un programa que reciba un nombre de usuario, luego de obtenerlo diga "Las computadoras dominaremos el mundo, @nombre"


nombre = input('Ingresa tu nombre, por favor.\n')

print('Las computadoras dominaremos al mundo, ' + nombre+ '.')

##################################################################################################################################


#Escribir un programa que reciba texto, si es una fruta y es una banana o manzana indica "yummi", si no lo es dice "puajjj"


fruta = input('Escriba el nombre de una fruta\n')

if fruta == 'banana' or fruta == 'manzana':
    print('yummi')
else:
    print('puajjj')

##################################################################################################################################


#Escribir un programa que reciba un número entero positivo, devolver la sumatoria de dicho número


def sumatoria(x):
    numero = input('ingrese un numero entero positivo\n')

    numero = int(numero) #transformo de tipo str a tipo int

    i=0
    j= 0
    for i in range (0, numero):


        i = i + 1 #contador que me hace salir del loop
        j = j + i #sumatoria
    return(j)

print(sumatoria(5))

##################################################################################################################################



#Modificar el ejercicio anterior generando que únicamente sume números que sean múltiplos de 3, 5 o 7 hasta el número ingresado.


def sumatoria_3_5_7(x):
    numero = input('ingrese un numero entero positivo\n')

    numero = int(numero) #transformo de tipo str a tipo int

    i=0
    j= 0
    for i in range (0, numero):


        i = i + 1 #contador que me hace salir del loop
        if i%3 == 0 or i%5 == 0 or i%7 == 0:

            j = j + i #sumatoria
            
    return(j)

print(sumatoria_3_5_7(10))

##################################################################################################################################


#Dado un numero ingresado por el usuario, dar la posibilidad al mismo de: generar su sumatoria o su factorial.


def sumatoria_o_factorial(x):
    numero = input('ingrese un numero entero positivo\n')
    decision = input('Si desea su sumatoria escriba 1, si desea su factorial escriba 2\n')

    if decision == '1':
        numero = int(numero)  # transformo de tipo str a tipo int

        i = 0
        j = 0
        for i in range(0, numero):
            i = i + 1  # contador que me hace salir del loop
            j = j + i  # sumatoria
        return (j)


    elif decision == '2':
        numero = int(numero)  # transformo de tipo str a tipo int

        i = 0
        j = 1 #inicio en 1 a diferencia de la sumatoria que iniciaba en 0
        for i in range(0, numero):
            i = i + 1  # contador que me hace salir del loop
            j = j * i  # sumatoria
        return (j)

print(sumatoria_o_factorial(10))


##################################################################################################################################

#Computar el número K ingresado! 4⋅∑(−1)i+12i . Ayudita: la sumatoria va de 0 a K, en este caso i es el elemento del ciclo.


def sumatoria_rara(k):
    i=0
    j= 0
    for i in range (0, k):

        i = i + 1 #contador que me hace salir del loop

        j = j +((-1)*i + 12*i) #sumatoria
        
    return(4*j)


print(sumatoria_rara(2))

##################################################################################################################################

#¿Que año es dentro de 20 años? (APA! consultame si necesitas!)


import time
import datetime

def futuro():
    futuro = datetime.date.today().strftime("%Y")
    return('Dentro de 20 años sera el año: ' + str(int(futuro) + 20))

print(futuro())

##################################################################################################################################

#SUPER HARD, vale 10 puntos para Griffindor: Escribir un piedra, papel o tijera de 1 ronda.

Ayudita: Vas a tener que buscar como hacer un #random con tus propias manos. 
'''

import random

def piedra_papel_o_tijera():
    pass

usuario = input('Escribi un numero: 1 para piedra, 2 para papel o 3 para tijera\n')

usuario = int(usuario)

compu = random.randint(1, 3)

resultado = [usuario,compu]
resultado_cheto = ['Vos elegiste: '+ str(usuario),'Yo elegi: ' + str(compu)]

if resultado == [1,3] or resultado == [2,1] or resultado == [3,2]:
    print('Ganaste! :D')
    print(resultado_cheto)
elif resultado == [3,1] or resultado == [1,2] or resultado == [2,3]:
    print('Perdiste :(')
    print(resultado_cheto)
else:
    print('Empate')
    print(resultado_cheto)







