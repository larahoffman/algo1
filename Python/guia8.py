# Archivos
import typing

# Ejercicio 1.1
def contar_lineas(nombre_archivo:str) -> int:
    archivo:typing.IO = open(nombre_archivo, "r")
    lineas:list[str] = archivo.readlines()

    archivo.close() # liberamos memoria

    return len(lineas)

#print(contar_lineas("pepe.txt"))

# Ejercicio 2
def clonar_sin_comentarios(nombre_archivo:str):
    archivo:typing.IO = open(nombre_archivo, "r")
    archivo_clonado:typing.IO = open("pepe-clonado.txt", "w")

    lineas:list[str] = archivo.readlines()

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
#clonar_sin_comentarios("pepe.txt")

# Pilas
from queue import LifoQueue as Pila

p = Pila()
p.put(1)
p.put(2) # apilar
p.get() # desapila el último elemento en ingresar (y devuelve el elemento)
p.empty() # ve si la pila está vacía o no - devuelve un valor booleano

import random

# Ejercicio 8
def generar_nros_al_azar(cantidad:int, desde:int, hasta:int) -> Pila:
    p = Pila()

    for _ in range(cantidad):
        valor:int = random.randint(desde,hasta)
        p.put(valor)

    return p

# p = generar_nros_al_azar(3,20,60)
# print(p.queue)

# Ejercicio 9
def cantidad_elementos(p: Pila) -> int:
    cantidad:int = 0

    paux = copiar_pila(p)

    while(not paux.empty()):
        paux.get()
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

#print(cantidad_elementos(mi_pila)) # el valor se pasa por referencia
#print(cantidad_elementos(mi_pila))

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

# Ejercicio 11
def esta_bien_balanceada(s:str) -> bool:
    pass

# Ejercicio 12
def evaluar_expresion(s:str) -> float:
    p = Pila()
    operandos:str = "+-*/"
    for char in s:
        if char != " " and char not in operandos:
            p.put(char)
        elif char != " " and char in operandos:
            numero1 = float(p.get())
            numero2 = float(p.get())

            if char == "+":
                suma:float = numero1 + numero2
                p.put(suma)
            elif char == "-":
                resta:float = numero2 - numero1
                p.put(resta)
            elif char == "*":
                multiplicacion:float = numero1 * numero2
                p.put(multiplicacion)
            elif char == "/":
                division:float = numero1 / numero2
                p.put(division)
    return p.get()

expresion = "3 4 + 5 * 2 -"
#print(evaluar_expresion(expresion))

#########################n
from queue import Queue as Cola

# Ejercicio 13
def generar_nros_al_azar(cantidad: int, desde:int, hasta:int) -> Cola:
    c = Cola()

    for _ in range(cantidad):
        valor:int = random.randint(desde, hasta)
        c.put(valor)

    return c

#c = generar_nros_al_azar(4, 43, 80)
#print(f"Cola: {c.queue}")

# Ejercicio 14
def cantidad_elementos(c:Cola) -> int:
    colaaux = Cola()
    cantidad:int = 0
    while(not c.empty()):
        elemento = c.get()
        colaaux.put(elemento)
        cantidad += 1
    while(not colaaux.empty()):
        elemento = colaaux.get()
        c.put(elemento)
    return cantidad

# cola = Cola()
# cola.put(1)
# cola.put(4)
# cola.put(6)
# cola.put(2)
# print(cantidad_elementos(cola))
# print(cola.queue) # chequeando que la cola siga igual (es de tipo IN)

# Ejercicio 15
def buscar_el_maximo(c:Cola[int]) -> int:
    colaaux = Cola()
    maximo:int = c.get()
    colaaux.put(maximo)
    # claramente es mejor usar la funcion auxiliar copiar_cola()
    while(not c.empty()):
        numero = c.get()
        colaaux.put(numero)
        if numero > maximo:
            maximo = numero
    while(not colaaux.empty()):
        numero = colaaux.get()
        c.put(numero)
    return maximo

# cola = Cola()
# cola.put(1)
# cola.put(4)
# cola.put(2)
# cola.put(7)
# print(buscar_el_maximo(cola))
# print(cola.queue) # chequeo

def copiar_cola(c: Cola) -> Cola:
    colaaux = Cola()
    res = Cola()

    while(not c.empty()):
        elem = c.get()
        colaaux.put(elem)
    while(not colaaux.empty()): # se va reconstruyendo
        elem = colaaux.get()
        c.put(elem)
        res.put(elem)
    return res

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

#print(jugar_carton_de_bingo([1,5,7,12,65,77,2,90,54,66,68,34], armar_secuencia_de_bingo()))

# Ejercicio 17 
# Cola: donde se van almacenando los pedidos de atencion. Cola[(prioridad, nombre_paciente, especialidad_medica)]
# Devuelve la cantidad de pacientes de la cola que tienen prioridad en el rango [1, 3].
def n_pacientes_urgentes(c:Cola[(int, str, str)]) -> int:
    colaaux = copiar_cola(c)
    cantidad:int = 0
    while(not colaaux.empty()):
        pedido:tuple = colaaux.get()
        if pedido[0] in range(1,4):
            cantidad +=1
    return cantidad

'''cola = Cola()
cola.put((3, "Pepe", "Traumatologia"))
cola.put((8, "Luciana", "Dermatologia"))
cola.put((1, "Anastasia", "Cardiologia"))
cola.put((5, "Ana", "Traumatologia"))
print(n_pacientes_urgentes(cola))'''

# Ejercicio 18
# Cola: [(NombreYApellido, DNI, Preferencial o no, Prioridad o no)]
# La atencion a los clientes se da por el siguiente orden: primero las personas que tienen prioridad, luego las que tienen cuenta
# bancaria preferencial y por ultimo el resto. Dentro de cada subgrupo de clientes, se respeta el orden de llegada.
def atencion_a_clientes(c:Cola[(str, int, bool, bool)]) -> Cola[(str, int, bool, bool)]:
    colaaux = copiar_cola(c)
    cola_prioridad = Cola()
    cola_preferencial = Cola()
    cola_resto = Cola()

    while(not colaaux.empty()):
        cliente:tuple = colaaux.get()

        if cliente[3] == True:
            cola_prioridad.put(cliente)
        elif cliente[2] == True:
            cola_preferencial.put(cliente)
        else:
            cola_resto.put(cliente)
    resultado = Cola()
    while(not cola_prioridad.empty()):
        cliente_prioritario = cola_prioridad.get()
        resultado.put(cliente_prioritario)
    while(not cola_preferencial.empty()):
        cliente_preferencial = cola_preferencial.get()
        resultado.put(cliente_preferencial)
    while(not cola_resto.empty()):
        otro_cliente = cola_resto.get()
        resultado.put(otro_cliente)
    return resultado

"""cola = Cola()
cola.put(("Preferencial 1", 43820465, True, False))
cola.put(("Prioritario 1", 43820465, True, True))
cola.put(("Prioritario 2", 43820465, False, True))
cola.put(("Random", 43820465, False, False))
cola.put(("Preferencial 2", 43820465, True, False))
print(atencion_a_clientes(cola).queue)"""


# Diccionarios #

# Ejercicio 19
def clonar_sin_espacios(nombre_archivo:str):
    archivo:typing.IO = open(nombre_archivo, "r")
    archivo_clonado:typing.IO = open("pepe-sin-espacios.txt", "w")

    lineas:list[str] = archivo.readlines()

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

#print(agrupar_por_longitud("pepe.txt"))