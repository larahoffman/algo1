# Ejercicio 1
import math
# 1.1
def imprimir_hola_mundo() -> None:
    # Inicializo la variable saludo
    mensaje: str = "Hola Mundo"
    print(mensaje)

# 1.2
def imprimir_un_verso() -> None:
    verso:str = "Hace frío y estoy lejos de casa \nHace tiempo que estoy sentado sobre esta piedra..."
    print(verso)

# 1.3
def raizDe2() -> float:
    raiz2:float = round(math.sqrt(2), 4)
    return raiz2

# 1.4
def factorial_de_dos() -> int:
    factorial2:int = math.factorial(2)
    return factorial2

# opcion 2
def factorial_2_bis() -> int:
    n:int = 2
    factorial:int = 1

    for nro in range(1, n + 1):
        factorial = factorial * nro
    return factorial

# 1.5
# perímetro de la circunferencia de radio 1
def perimetro() -> None:
    perimetro:float = 2 * math.pi
    print(perimetro)


# Ejercicio 2

# 2.1
def imprimir_saludo(nombre:str):
    print(f"Hola {nombre}")

#imprimir_saludo("Pepe")

# 2.2
def raiz_cuadrada_de(numero:int)-> float:
    return math.sqrt(numero)

#print(raiz_cuadrada_de(8))

# 2.3 Convierte una temperatura en grados Fahrenheit a grados Celcius
def farenheit_a_celsius(temp_far:float) -> float:
    resultado:float = ((temp_far - 32) * 5) / 9
    return resultado

#print(farenheit_a_celsius(400.0))

# 2.4
def imprimir_dos_veces(estribillo: str) -> None:
    print(estribillo * 2)

#imprimir_dos_veces("Oh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh\nCaught in a bad romance\nOh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh\nCaught in a bad romance\n")

# 2.5
def es_multiplo_de(n: int, m:int) -> bool:
    # opción 1
    # resto:int = n % m # n módulo m
    # resultado:bool = resto == 0
    # return resultado
    # opción 2
    resto:int = n % m
    if resto == 0:
        return True
    else:
        return False

# 2.6 usar funcion del ej 2.5
def es_par(numero:int) -> bool:
    resultado:bool = es_multiplo_de(numero, 2)
    return resultado

# print(es_par(15))
# print(es_par(16))

# 2.7
def cantidad_de_pizzas(comensales:int, min_cant_de_porciones:int) -> int:
    cant_pizzas:int = (comensales * min_cant_de_porciones) // 8
    return math.ceil(cant_pizzas)
#ceil devuelve el entero mas cercano
#print(cantidad_de_pizzas(13,5))

# Ejercicio 3. Sin usar if, solo con and, or, not

# 3.1
def alguno_es_0(numero1:float, numero2:float) -> bool:
    condicion:bool = (numero1 == 0) or (numero2 == 0)
    return condicion

#print(alguno_es_0(1,1))

# 3.2
def ambos_son_0(numero1:float, numero2:float) -> bool:
    condicion:bool = (numero1 == 0) and (numero2 == 0)
    return condicion

#print(ambos_son_0(0,0))

# 3.3
def es_nombre_largo(nombre:str) -> bool:
    longitud:int = len(nombre)
    condicion:bool = longitud >= 3 and longitud <= 8
    resultado:bool = False
    if condicion:
        resultado:bool = True
    return resultado

# 3.4
def es_bisiesto(anio) -> bool:
    condicion:bool = es_multiplo_de(anio, 400) or (es_multiplo_de(anio, 4) and not(es_multiplo_de(anio, 100)))
    return condicion

print(es_bisiesto(2021))

# Ejercicio 5

# 5.1 devuelve el doble del numero en caso de ser par y el mismo numero en caso contrario
def devolver_el_doble_si_es_par(numero:int) -> int:
    es_par:bool = (numero % 2) == 0
    if es_par:
        numero = 2 * numero
    return numero

# Ejercicio 6

# 6.2 Escribir una función que imprima los números pares entre el 10 y el 40
def imprimir_pares_10_40() -> None:
    numero:int = 10
    while(numero <= 40):
        print(numero)
        numero = numero + 2

# 6.4 Escribir una función de cuenta regresiva para lanzar un cohete. Dicha función ira imprimiendo desde el numero que me pasan por parametro (que sera positivo) 
# hasta el 1, y por ultimo “Despegue”

def cuenta_regresiva(numero:int) -> str:
    i: int = 1

    while (i <= numero):
        print(numero)
        numero -= 1
    # otra opción
    # for i in range(numero,0, -1):
    #     print(i)
    print("Despegue")
    