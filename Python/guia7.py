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

#Ejercicio 1.4
def ordenados(seq:list[int])->bool:
    for i in range(0,len(seq)-1):
        if (not(seq[i]<seq[i+1])):
            return False
    return True


#print(ordenados([3,2,4]))

# Ejercicio 1.5. Dada una lista de palabras, devolver verdadero si alguna palabra tiene longitud mayor a 7
def mas_de_siete_caracteres(s:list[str]) -> bool:
    mas_de_siete:bool = False

    for palabra in s:
        longitud_palabra:int = len(palabra)
        if longitud_palabra > 7:
            mas_de_siete = True
    return mas_de_siete

#print(mas_de_siete_caracteres(["hola", "pepeeeeeee"]))


def es_palindromo(texto:str)->bool:
    longitud:int=len(texto)
    for i in range(0,longitud // 2):
        if texto[i] != " ":
            if(texto[i]!=texto[(longitud-1)-i]):
                return False
    return True

# print(es_palindromo("neuquen"))
# print(es_palindromo("ojo rojo"))
# print(es_palindromo("hola"))
# print(es_palindromo("dabale arroz a la zorra el abad")) este no funciona

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

# Ejercicio 1.8 Dada una lista de tuplas, que representa un historial de movimientos en una cuenta bancaria, devolver el saldo actual.
def saldo_actual(movimientos:list[tuple]) -> int:
    saldo:int = 0
    ingreso:str = 'I'
    retiro:str = 'R'

    for i in range(0, len(movimientos)):
        if movimientos[i][0] == ingreso:
            saldo += movimientos[i][1]
        elif movimientos[i][0] == retiro:
            saldo -= movimientos[i][1]
    return saldo
# otra manera
def saldo_actual_PM(movimientos: list[tuple[str, int]]) -> int:
    saldo:int = 0
    for tipo_movimiento, dinero in movimientos:
        if tipo_movimiento == 'I':
            saldo += dinero
        elif tipo_movimiento == 'R':
            saldo -= dinero
    return saldo

#print(saldo_actual([('I', 2000), ('R', 20), ('R', 1000), ('I', 300)])) da 1280

# Ejercicio 1.9 Recorrer una palabra en formato string y devolver True si esta tiene al menos 3 vocales distintas y False en caso contrario
def tiene_tres_vocales_distintas(palabra: str) -> bool:
    vocales = "aeiouAEIOU"
    vocales_encontradas = []
    resultado:bool = False

    for letra in palabra:
        if letra in vocales and letra not in vocales_encontradas:
            vocales_encontradas.append(letra)
        if len(vocales_encontradas) >= 3:
            resultado = True

    return resultado

# print(tiene_tres_vocales_distintas("pepe"))
# print(tiene_tres_vocales_distintas("murcielago"))
# print(tiene_tres_vocales_distintas("aereo"))

# Clase 27-05
# https://pastebin.com/xabaQTyv

# Ejercicio 2.1 La lista es de tipo inout

def es_par(n:int) -> bool:
    return (n % 2 == 0)

def reemplaza_posiciones_pares(s:list[int]) -> list[int]:
    i:int = 0
    longitud:int = len(s)

    while i < longitud:
        if (es_par(i)):
            s[i] = 0
        i += 1
    
    return s

def reemplaza_posiciones_pares2(s:list[int]) -> list[int]:
    i:int = 0
    longitud:int = len(s)

    while i < longitud:
        s[i] = 0
        i += 2
    return s

def reemplaza_posiciones_pares_for(s:list[int]) -> list[int]:
    for i in range(0, len(s), 2):
        s[i] = 0
    return s
        

# lista = [3,5,6]
# reemplaza_posiciones_pares_for(lista)
#print(f"Lista nueva: {lista}")

# Ejercicio 2.2 La lista es de tipo in (no se puede modificar)
def reemplaza_posiciones_pares_for_in(s:list[int]) -> list[int]:
    lista:list[int] = []
    for i in range(0, len(s)):
        if es_par(i):
            lista.append(0)
        else:
            lista.append(s[i])
    return lista

# lista = [3,5,6,5,5,7,2,1]
# print(reemplaza_posiciones_pares_for_in(lista)) -> [0, 5, 0, 5, 0, 7, 0, 1]
# print(lista) -> [3, 5, 6, 5, 5, 7, 2, 1]

# Ejercicio 2.3
def sin_vocales(cadena:str) -> str:
    vocales:str = "aeiouAEIOU"
    lista:str = ""

    for i in range(0, len(cadena)):
        caracter:str = cadena[i]
        if caracter not in vocales:
            lista += caracter
    return lista

# cadena = "Habia una vez"
# print(sin_vocales(cadena))

# Ejercicio 2.4
def reemplaza_vocales(s:list[chr]) -> list[chr]:
    vocales:str = "aeiouAEIOU"
    lista:list[chr] = []

    for i in range(0, len(s)):
        caracter:str = s[i]
        if caracter not in vocales:
            lista.append(caracter)
        else:
            lista.append('')
    return lista

#print(reemplaza_vocales(['a', 'b', 'c', 'd', 'e']))

# Ejercicio 2.5
def da_vuelta_str(s:list[chr]) -> list[chr]:
    s_reverso:list[chr] = []
    longitud:int = len(s)

    for i in range(0,longitud):
        s_reverso += s[longitud - i - 1]
    return s_reverso

#print(da_vuelta_str(['a', 'b', 'c', 'd']))

# para numeros
def reverso(s:list[int]) -> list[int]:
    s_reverso:list[int] = []
    longitud:int = len(s)

    for i in range(0,longitud):
        s_reverso.append(s[longitud - i - 1])
    return s_reverso

#print(reverso([1,2,3,4]))

# Ejercicio 2.6
def eliminar_repetidos(s:list[chr]) -> list[chr]:
    lista_nueva:list[chr] = []
    longitud:int = len(s)

    for i in range(0, longitud):
        if s[i] not in lista_nueva:
            lista_nueva.append(s[i])
    return lista_nueva

#print(eliminar_repetidos("abcddfreet"))

# Ejercicio 3
def aprobado(notas:list[int]) -> int:
    longitud:int = len(notas)
    promedio:int = suma_total(notas) // longitud
    resultado:int = 0

    for nota in notas:
        if nota >= 4:
            if promedio >= 7:
                resultado = 1
            elif promedio >= 4 and promedio < 7:
                resultado = 2
        else:
            resultado = 3
    return resultado

# print(aprobado([4,6,7,6,9,10]))
# print(aprobado([1,4,7,8,2]))
# print(aprobado([4,4,4,4,4]))

# Ejercicio 4
# 4.1
def estudiantes() -> list[str]:
    nombre = input("Ingrese el nombre del estudiante o 'Listo' para finalizar: ")
    lista_estudiantes:list[str] = []
    while(nombre != "Listo"):
        lista_estudiantes.append(nombre)
        nombre = input("Ingrese el nombre del estudiante o 'Listo' para finalizar: ")
    return lista_estudiantes
#print(estudiantes())

# 4.2
def historial_monedero_electronico() -> list[tuple[str, int]]:
    monedero:list[tuple[str, int]] = []
    print("Menu Monedero")
    print("'C' - Cargar creditos\n'D' - Descontar creditos\n'X' - Salir")
    accion = input("Ingrese la letra correspondiente a la accion que desea realizar: ")

    while(accion != "X"):
        if accion == "C":
            monto = int(input("Ingrese el monto a cargar: "))
            monedero.append((accion,monto))
        elif accion == "D":
            monto = int(input("Ingrese el monto a descontar: "))
            monedero.append((accion,monto))
        print("\nMenu Monedero")
        print("'C' - Cargar creditos\n'D' - Descontar creditos\n'X' - Salir")
        accion = input("Ingrese la letra correspondiente a la accion que desea realizar: ")
    return monedero

#print(historial_monedero_electronico())

# Ejercicio 5

# Ejercicio 5.1
def pertenece_a_cada_uno_version_1(s:list[list[int]], e:int, res:list[bool]) -> None:
    
    for valor in s:
        res.append(pertenece2(valor, e))
    print(res)

#pertenece_a_cada_uno_version_1([[1,2,3,4], [4,5], [3,3]], 4, [True, False])

# La diferencia esta en limpiar res al principio ?

# Ejercicio 5.2
def pertenece_a_cada_uno_version_2(s:list[list[int]], e:int, res:list[bool]) -> None:
    res.clear() # recomendado hacer siempre para variables de tipo out -> tambien se puede hacer res = []

    for valor in s:
        res.append(pertenece2(valor, e))

# Ejercicio 5.3
def es_matriz(m: list[list[int]]) -> bool:
    
    longitud_fila = len(m[0])
    for fila in m:
        if len(fila) != longitud_fila:
            return False
    return True
#print(es_matriz([[1, 2, 3], [4, 5, 6], [7, 8]])) False
# print(es_matriz([[1,2,3], [4,5,6]])) True
# print(es_matriz([[1,2],[3,5,6],[4,3]])) False

# Ejercicio 5.4
def filas_ordenadas(m:list[list[int]], res: list[bool]) -> None:
    res = []
    for fila in m:
        valor:bool = False
        if ordenados(fila):
            valor = True
        res.append(valor)
    print(res)
# filas_ordenadas([[1,2,3], [4,5,6]], [True,False])
# filas_ordenadas([[4,2,3], [4,5,6], [2,1,6], [9,9,10]], [True,False])

# Ejercicios inventados por mi
def recorrer_filas(matriz:list[list[int]]) -> None:
    '''Las filas son los elementos de la lista de listas'''
    for fila in matriz:
        print(fila)

matriz = [[4,2,3], [4,5,6], [2,1,6], [9,9,10]]
#recorrer_filas(matriz)

def recorrer_columnas(matriz:list[list[int]]) -> None:
    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    for columna in range(num_columnas):
        for fila in range(num_filas):
            print(matriz[fila][columna])

#recorrer_columnas(matriz)

def transponer_matriz(matriz: list[list[int]]) -> list[list[int]]:
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    
    # Crea una nueva matriz de tamaño num_columnas x num_filas (en vez de m x n -> n x m)
    matriz_transpuesta = []
    for _ in range(num_columnas):
        matriz_transpuesta.append([])
    print(matriz_transpuesta)
    
    for fila in range(num_filas):
        for columna in range(num_columnas):
            matriz_transpuesta[columna].append(matriz[fila][columna])

    return matriz_transpuesta

#print(transponer_matriz(matriz))
