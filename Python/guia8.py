# Clase 29-05

# Pilas
from queue import LifoQueue as Pila

p = Pila()
p.put(1) #apilar
elemento = p.get() #desapila el último elemento en ingresar (devuelve el elemento)
p.empty() #vacía - devuelve un valor booleano

##########################################

def contar_elementos_pila(p: Pila) -> int:
    cantidad:int = 0

    paux = copiar_pila(p)

    while(not paux.empty()):
        elem = paux.get()
        cantidad += 1
    
    return cantidad
# no existe la función copy() para las pilas, entonces hay que hacerlo manualmente
def copiar_pila(p: Pila) -> Pila:
    paux = Pila()
    res = Pila()

    while(not p.empty()):
        elem = p.get()
        paux.put(elem)
    while(not paux.empty()): # se va reconstruyendo
        elem = paux.get()
        p.put(elem)
        res.put(elem)
    return res
# esta función es particularmente útil para cuando, en la especificación, el parámetro de entrada es de tipo IN y no se puede modificar su valor

mi_pila = Pila()
mi_pila.put(2)
mi_pila.put(8)
mi_pila.put(8)
mi_pila.put(5)

#print(contar_elementos_pila(mi_pila)) # el valor se pasa por referencia
#print(contar_elementos_pila(mi_pila))

import random

# Ejercicio 8
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila:
    p = Pila()

    for k in range(cantidad):
        valor:int = random.randint(desde,hasta)
        p.put(valor)

    return p

p = generar_nros_al_azar(3,20,60)
#print(p.queue)

# Ejercicio 10
def buscar_el_maximo(p:Pila) -> int:
    '''Devuelve el máximo elemento'''
    paux = copiar_pila(p)
    res:int = paux.get()

    while(not paux.empty()):
        elemento = paux.get()

        if elemento > res:
            res = elemento
    return res

mi_pila = Pila()
mi_pila.put(2)
mi_pila.put(8)
mi_pila.put(8)
mi_pila.put(5)
#print(buscar_el_maximo(mi_pila))

# Archivos
import typing

# Ejercicio 1.1
def contar_lineas(nombre_archivo:str) -> int:
    archivo:typing.IO = open(nombre_archivo, "r")
    lineas:[str] = archivo.readlines()

    archivo.close() # liberamos memoria

    return len(lineas)

#print(contar_lineas("pepe.txt"))

# Ejercicio 2
def clonar_sin_comentarios(nombre_archivo:str):
    archivo:typing.IO = open(nombre_archivo, "r")
    archivo_clonado:typing.IO = open("pepe-clonado.txt", "w")

    lineas:[str] = archivo.readlines()

    for linea in lineas:
        if not (es_comentario(linea)):
            archivo_clonado.write(linea)
    
    archivo.close()
    archivo_clonado.close()

def es_comentario(linea:str) -> bool:
    res:bool = False

    for e in linea:
        if e == "#":
            res = True
    return res

#print(es_comentario("elpepe"))
#print(es_comentario("#jujuju"))
#print(es_comentario("                 #"))
clonar_sin_comentarios("pepe.txt")

#########################n
from queue import Queue as Cola

# Ejercicio 13
def generar_nros_al_azar(cantidad: int, desde:int, hasta:int) -> Cola:
    c = Cola()

    for _ in range(cantidad):
        valor:int = random.randint(desde, hasta)
        c.put(valor)

    return c

c = generar_nros_al_azar(4, 43, 80)
#print(f"Cola: {c.queue}")

# Ejercicio 16. Un cartón de bingo contiene 12 números al azar en el rango [0, 99].
# 16.1.
def armar_secuencia_de_bingo()-> Cola[int]:
    lista:list = list(range(0,100))

    random.shuffle(lista)

    bolillero: Cola = Cola()

    for bolilla in lista:
        bolillero.put(bolilla)

    return bolillero

#print(armar_secuencia_de_bingo().queue)

# 16.2

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    bolillero_aux:Cola = Cola()
    cantidad_sin_marcar:int = len(carton)
    jugadas:int = 0

    while cantidad_sin_marcar > 0:
        num:int = bolillero.get()
        bolillero_aux.put(num)

        if num in carton:
            cantidad_sin_marcar -= 1
        jugadas += 1
    
    while (not bolillero.empty()): #hay que volver a armar la cola
        num:int = bolillero.get()
        bolillero_aux.put(num)
    while (not bolillero_aux.empty()):
        num:int = bolillero_aux.get()
        bolillero.put(num)        

    return jugadas

print(jugar_carton_de_bingo([1,5,7,12,65,77,2,90,54,66,68,34], armar_secuencia_de_bingo()))

# Diccionarios #

# Ejercicio 19
def clonar_sin_espacios(nombre_archivo:str):
    archivo:typing.IO = open(nombre_archivo, "r")
    archivo_clonado:typing.IO = open("pepe-sin-espacios.txt", "w")

    lineas:[str] = archivo.readlines()

    for linea in lineas:
        if not (es_espacio(linea)):
            archivo_clonado.write(linea)
    
    archivo.close()
    archivo_clonado.close()

def es_espacio(linea:str) -> bool:
    res:bool = False

    for e in linea:
        if e == " ":
            res = True
    return res

def agrupar_por_longitud(nombre_archivo:str) -> dict:
    archivo:typing.IO = open(nombre_archivo, "r")
    d:dict = {}

    for linea in archivo.readlines():
        palabras = linea.split() # no se puede usar en el parcial
        for palabra in palabras:
            clave = len(palabra)
            if clave in d:
                d[clave] = d[clave] + 1
            else:
                d[clave] = 1
    
    archivo.close()
    return d

print(agrupar_por_longitud("pepe.txt"))