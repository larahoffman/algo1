# Ejercicio 1.1

def pertenece(s:list[int], e: int) -> bool:
    i: int = 0
    longitud: int = len(s)
    resultado: bool = False
    
    while (i < longitud):
        valor: int = s[i]

        if (e == valor):
            resultado = True
        i += 1

    return resultado

#print(pertenece([1,3,2,3], 4))

def pertenece2(s:list[int], e:int) -> bool:
    resultado: bool = False
    for elemento in s:
        if (e == elemento):
            resultado = True
    return resultado

#print(pertenece2([1,3,2,3], 1))

# Ejercicio 1.2
def divide_a_todos(s:list[int], e:int) -> bool:
    divide:bool = True

    for numero in s:
        if not(numero % e == 0):
            divide = False
    return divide

#print(divide_a_todos([1,4,4], 1))

# Ejercicio 1.3

def suma_total(s:list[int]) -> int:
    total:int = 0
    indice:int = 0
    longitud:int = len(s)

    while (indice < longitud):
        valor:int = s[indice]
        total += valor
        indice += 1

    return total

#print(suma_total([1,2,3]))

# Ejercicio 1.4
def ordenados(s:list[int]) -> bool:
    longitud: int = len(s)
    i: int = 0
    j: int = 0
    ordenado:bool = False

    while i < longitud:
        if s[i] <= s[j]:
            ordenado = True
        i += 1
        j += 1
    return ordenado

ordenados([3,2,4])


# Ejercicio 1.7 Fortaleza de una contraseña
def ver_fortaleza_contrasenia(contrasenia:str) -> str:
    longitud: int = len(contrasenia)
    valor:str = ""

    if longitud < 5:
        valor = "ROJA"
    elif longitud > 8:
        for c in contrasenia:
            pass
        valor = "VERDE"
    else:
        valor = "AMARILLA"

    return valor

# Clase 27-05
# https://pastebin.com/xabaQTyv
# Ejercicio 2.1

def es_par(n:int) -> bool:
    return (n % 2 == 0)

def reemplaza_pares(s:list[int]) -> None:
    i:int = 0
    longitud:int = len(s)

    while i < longitud:
        if (es_par(i)):
            s[i] = 0
        i += 1

def reemplaza_pares2(s:list[int]) -> No# Clase 27-05
# https://pastebin.com/xabaQTyv
# Ejercicio 2.1

def es_par(n:int) -> bool:
    return (n % 2 == 0)

def reemplaza_pares(s:list[int]) -> None:
    i:int = 0
    longitud:int = len(s)

    while i < longitud:
        if (es_par(i)):
            s[i] = 0
        i += 1

def reemplaza_pares2(s:list[int]) -> None:
    i:int = 0
    longitud:int = len(s)

    while i < longitud:
        s[i] = 0
        i += 2

def reemplaza_pares_for(s:list[int]) -> None:
    for i in range(0, len(s), 2):
        s[i] = 0
        

lista = [3,5,6]
reemplaza_pares_for(lista)
print(f"Lista nueva: {lista}")

# Ejercicio 5.2
def pertenece_a_cada_uno_version_2(s:list[list[int]], e:int, res:list[bool]) -> None:
    res.clear() # recomendado hacer siempre para variables de tipo out

    for valor in s:
    #    if pertenece(valor,e):
    #        res.append(True)
    #    else:
    #        res.append(False)
        res.append(pertenece2(valor, e))

s = [[5,6], [2], [1,2]]
res = []

pertenece_a_cada_uno_version_2(s, 5, res)

print(f"Resultado: {res}")ne:
    i:int = 0
    longitud:int = len(s)

    while i < longitud:
        s[i] = 0
        i += 2

def reemplaza_pares_for(s:list[int]) -> None:
    for i in range(0, len(s), 2):
        s[i] = 0
        

lista = [3,5,6]
reemplaza_pares_for(lista)
print(f"Lista nueva: {lista}")

# Ejercicio 5.2
def pertenece_a_cada_uno_version_2(s:list[list[int]], e:int, res:list[bool]) -> None:
    res.clear() # recomendado hacer siempre para variables de tipo out

    for valor in s:
    #    if pertenece(valor,e):
    #        res.append(True)
    #    else:
    #        res.append(False)
        res.append(pertenece2(valor, e))

s = [[5,6], [2], [1,2]]
res = []

pertenece_a_cada_uno_version_2(s, 5, res)

print(f"Resultado: {res}")
