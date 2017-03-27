'''Tuplas, listas y diccionarios - Estructuras de control de flujo, Bucles

# Escribir un listado de famosos en un archivo .py. Desde otro archivo mostrar por pantalla el listado de famosos numerados.
#Esta hecho en dos arhivos separados

#####################################################################################################################################################################################################

# Se requiere ingresar por pantalla notas de alumnos y sus respectivos nombres. Los nombres deberán contener minimamente 5 caracteres y su nota será entre 0 y 10.
Es necesario calcular el promedio de los alumnos.
'''

boletin = {}



nombre = input('ingrese el nombre del alumno. Minimo 5 caracteres\n')
if len(nombre)<5:
    print('El nombre a ingresar debe tener al menos 5 caracteres')

else:


    nota = input('ingrese la nota del alumno con un valor entre 0 y 10\n')
    nota = int(nota)
    boletin[nombre] = nota
    otro_dato = input('Desea agregar otro alumno? Escriba si o no y presione enter.\n')


    if otro_dato == 'si':
        nombre = input('ingrese el nombre del alumno\n')
        nota = input('ingrese la nota del alumno\n')
        nota = int(nota)
        boletin[nombre] = nota
        otro_dato = input('Desea agregar otro alumno? Escriba si o no y presione enter.\n')
        if otro_dato == 'no':
            boletin[nombre] = nota
            nota = int(nota)
            nota = boletin.values()


            promedio = (sum(nota) / len(nota))

            print(promedio)


    elif otro_dato == 'no':
        boletin[nombre] = nota
        nota = boletin.values()
        promedio = (sum(nota) / len(nota))

        print(promedio)







''''
- Se requiere ingresar por pantalla materias de la carrera. La materia se compone con: número de 5 cifras de identificación única, un nombre y un listado de alumnos (con sus notas).

- Dada una cadena de texto de 10 a 20 caracteres ingresada por el usuario quedarse con los primeros 3 y los ultimos 5.

- Se debera generar un sistema que mantenga en memoria datos de una agenda.
    - El programa mostrara las opciones> agregar, editar, borrar, mostrar y salir
    agregar, agenda un contacto (email, telefono, nombre, domicilio, edad y dni)
    editar, permite modificar cualquiera de los contactos seleccionando su email.
    borrar, elimina un contacto. '''