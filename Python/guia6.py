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

#print(es_bisiesto(2021))

# Ejercicio 4. Resolver usando min y max

# 4.1
def peso_pino(altura:int) -> int:
    peso:int = 0

    if altura > 0 and altura <= 3:
        peso = (altura * 100) * 3
    else:
        peso += (300 * 3) + ((altura - 3) * 100) * 2

    return peso

# 4.2
def es_peso_util(peso:int) -> bool:
    rango:list = range(400, 1001)
    resultado:bool = False

    if peso in rango:
        resultado = True
    return resultado

#print(peso_pino(1)) 300kg
#print(es_peso_util(800)) True

# 4.3
def sirve_pino(altura:int) -> bool:
    return es_peso_util(peso_pino(altura))

#print(sirve_pino(1)) False

# Ejercicio 5

# 5.1 devuelve el doble del numero en caso de ser par y el mismo numero en caso contrario
def devolver_el_doble_si_es_par(numero:int) -> int:
    es_par:bool = (numero % 2) == 0
    if es_par:
        numero = 2 * numero
    return numero

# 5.2
def devolver_valor_si_es_par_sino_el_que_sigue(numero:int) -> int:
    if es_par(numero):
        return numero
    else:
        return numero + 1

#print(devolver_valor_si_es_par_sino_el_que_sigue(3))

# 5.3
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:int) -> int:
    multiplo3:bool = numero % 3 == 0
    multiplo9:bool = numero % 9 == 0

    if multiplo9:
        return numero * 3
    elif multiplo3:
        return numero * 2
    else:
        return numero

# print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(4))
# print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(6))
# print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(18))
# print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(15))

# 5.4
def lindo_nombre(nombre:str) -> str:
    if len(nombre) >= 5:
        return "Tu nombre tiene muchas letras!"
    else:
        return "Tu nombre tiene menos de 5 caracteres"

# 5.5
def elRango(numero:int) -> None:
    if numero < 5:
        print("Menor a 5")
    elif numero >= 10 and numero <= 20:
        print("Entre 10 y 20")
    elif numero > 20:
        print("Mayor a 20")

# elRango(5) para los numeros entre el 5 y el 9 no hace nada

# 5.6
def vacaciones_o_trabajo(sexo:str, edad:int) -> None:
    menor_edad:bool = edad < 18
    jubilada_F:bool = sexo == 'F' and edad >= 60
    jubilado_M:bool = sexo == 'M' and edad >= 65

    if menor_edad or jubilada_F or jubilado_M:
        print("Anda de vacaciones")
    else:
        print("Te toca trabajar")

# vacaciones_o_trabajo("M",15)
# vacaciones_o_trabajo("F",34)
# vacaciones_o_trabajo("M",61)
# vacaciones_o_trabajo("F",78)

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
    