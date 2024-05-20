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

# 1.5
# perímetro de la circunferencia de radio 1
def perimetro() -> None:
    perimetro:float = 2 * math.pi
    print(perimetro)


# Ejercicio 2

# 2.1
def imprimir_saludo(nombre:str):
    pass

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

# Ejercicio 3

# 3.3
def es_nombre_largo(nombre:str) -> bool:
    longitud:int = len(nombre)
    condicion:bool = longitud >= 3 and longitud <= 8
    resultado:bool = False
    if condicion:
        resultado:bool = True
    return resultado

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
    