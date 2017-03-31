'''Tuplas, listas y diccionarios - Estructuras de control de flujo, Bucles

# Escribir un listado de famosos en un archivo .py. Desde otro archivo mostrar por pantalla el listado de famosos numerados.
#Esta hecho en dos arhivos separados

#####################################################################################################################################################################################################

# Se requiere ingresar por pantalla notas de alumnos y sus respectivos nombres. Los nombres deberán contener minimamente 5 caracteres y su nota será entre 0 y 10.
Es necesario calcular el promedio de los alumnos.

def promedio(nota):

    promedio = (sum(nota) / len(nota))
    return 'El promedio de las notas es: ' + str(promedio)

def entrada_boletin(otro_dato):
    nombre = input('ingrese el nombre del alumno. Minimo 5 caracteres\n')
    if len(nombre) > 4:
        nota = input('ingrese la nota del alumno con un valor entre 0 y 10\n')
        nota = int(nota)
        if -1 < nota < 11:
            nota = int(nota)
            boletin[nombre] = nota
            nota = boletin.values()
            otro_dato = input('Desea agregar otro alumno? Escriba si o no y presione enter.\n')

    if otro_dato == 'si':
        return entrada_boletin(otro_dato)

    elif otro_dato == 'no':
        print (promedio(nota))
#main

# Creo un diccionario vacio
boletin = {}
#inicializo la variable otro_dato
otro_dato = 'asd'

entrada_boletin(otro_dato)
if otro_dato == 'si':
    entrada_boletin(otro_dato)
    if otro_dato == 'no':
        print(promedio(nota))
elif otro_dato == 'no':
    print(promedio(nota))
    
#################################################################################################################################################



- Se requiere ingresar por pantalla materias de la carrera. La materia se compone con: número de 5 cifras de identificación 
única, un nombre y un listado de alumnos (con sus notas).
'''

def entrada_boletin(otro_dato):
    nombre = input('ingrese el nombre del alumno. Minimo 5 caracteres\n')
    if len(nombre) > 4:
        nota = input('ingrese la nota del alumno con un valor entre 0 y 10\n')
        nota = int(nota)
        if -1 < nota < 11:
            nota = int(nota)
            boletin[nombre] = nota



            materias.append(nota)
            otro_dato = input('Desea agregar otro alumno? Escriba si o no y presione enter.\n')

    if otro_dato == 'si':
        return entrada_boletin(otro_dato)

    elif otro_dato == 'no':
        print (materias)

materias = []
boletin = {}
otro_dato = 'asd'

numero = input('ingrese el numero de materia. El mismo debera tener 5 digitos.\n')
materias.append(numero)
nombre = input('ingrese el nombre de la materia. El mismo debera tener 5 digitos.\n')
materias.append(nombre)
entrada_boletin(otro_dato)
if otro_dato == 'si':
    entrada_boletin(otro_dato)
    if otro_dato == 'no':
        print (materias)
elif otro_dato == 'no':
    print (materias)





'''

- Dada una cadena de texto de 10 a 20 caracteres ingresada por el usuario quedarse con los primeros 3 y los ultimos 5.

- Se debera generar un sistema que mantenga en memoria datos de una agenda.
    - El programa mostrara las opciones> agregar, editar, borrar, mostrar y salir
    agregar, agenda un contacto (email, telefono, nombre, domicilio, edad y dni)
    editar, permite modificar cualquiera de los contactos seleccionando su email.
    borrar, elimina un contacto.

'''
