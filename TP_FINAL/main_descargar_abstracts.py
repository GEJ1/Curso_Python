# -*- coding: utf-8 -*-

SYSTEM_MOVIES = [
    {
        "nombre" : "La sirenita",
        "descripcion" : "La ninia pez sin piernas"
    }
]

MENSAJE_BIENVENIDA = '''
##############################################
    Bienvenido a CHOITS CINEMA SYSTEM
##############################################\n\n
'''
OPCIONES_SISTEMA = ["Agregar pelicula", "Ver peliculas disponibles"]
OPCIONES_PELICULA = ["Ver asientos disponibles", "Reservar", "Ver descripcion"]

def ingrese_nombre_pelicula():
    return str(raw_input("ingrese pelicula>"))

def ingrese_descripcion_pelicula():
    return str(raw_input("ingrese descripcion>"))

def resolver_menu(opcion):
    if opcion == 1:
        nombre = ingrese_nombre_pelicula()
        descripcion = ingrese_descripcion_pelicula()
        dictionary = dict()
        dictionary["nombre"] = nombre
        dictionary["descripcion"] = descripcion #que otras opciones de diccionario hay?
        SYSTEM_MOVIES.append(dictionary)
        print("Pelicula ingresada exitosamente.")
        menu_inicio()
    else: #es opcion 2 unicamente, porque lo protegimos
        print(SYSTEM_MOVIES)



def validar_opcion(opcion, es_menu_principal=True):
    if es_menu_principal and type(opcion) == int and opcion > 0 and opcion < 3:
        resolver_menu(opcion)
    elif not es_menu_principal and type(opcion) == int and opcion > 0 and opcion < 4:
        pass
    else:
        print("Opcion invalida :()")
        capturar_ingreso_usuario()

def capturar_ingreso_usuario():
    option = int(raw_input("Ingrese la opcion deseada>"))
    return option


def mostrar_opciones(opciones):
    indice = 1
    for opt in opciones:
        print(str(indice) + ">" + opt)
        indice = indice + 1

def saludar():
    print(MENSAJE_BIENVENIDA)

def menu_inicio():
    mostrar_opciones(OPCIONES_SISTEMA)
    opcion = capturar_ingreso_usuario()
    validar_opcion(opcion)

def iniciar_sistema():
    saludar()
    menu_inicio()


if __name__ == '__main__':
    iniciar_sistema()
