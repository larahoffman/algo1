# Ejercicio 1.1

def pertenece(s:list[int], e: int) -> bool:
    i: int = 0
    longitud: int = len(s)

    while (i < longitud):
        valor: int = s[i]
        resultado: bool = False

        if (e == valor):
            resultado = True
        i += 1

    return resultado

print(pertenece([1,3,2,3], 4))

def pertenece2(s:list[int], e:int) -> bool:
    resultado: bool = False
    for elemento in s:
        if (e == elemento):
            resultado = True
    return resultado

print(pertenece2([1,3,2,3], 1))

#Ejercicio 1.3

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
