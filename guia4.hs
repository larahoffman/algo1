-- Ej 1. Implementar la funcion fibonacci: Integer -> Integer que devuelve el i-esimo numero de Fibonacci

fibonacci :: Integer -> Integer
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | n >= 2 = fibonacci(n-1) + fibonacci(n-2)
-- con pattern matching
fibonacci2 :: Integer -> Integer
fibonacci2 0 = 0
fibonacci2 1 = 1
fibonacci2 n = fibonacci2(n-1) + fibonacci2(n-2)

-- Ej 2. Implementar una funcion parteEntera :: Float -> Integer

parteEntera :: Float -> Integer
parteEntera x | x < 1 && x >= 0 = 0
              | x >= 1 = 1 + parteEntera(x-1)
              | otherwise = (-1) + parteEntera(x+1) -- no me da bien

-- Ej 3. Especificar e implementar la funcion esDivisible :: Integer ->Integer -> Bool que dados dos numeros 
-- naturales determinar si el primero es divisible por el segundo. No esta permitido utilizar las funciones mod ni div.

-- esDivisible :: Integer -> Integer -> Bool
-- requiere: x > 0, y > 0
-- asegura: x > y, y multiplo de x

esDivisible :: Integer -> Integer -> Bool
esDivisible _ 0 = False -- no se puede dividir por 0
esDivisible m n | m < n = False
                | m == n = True
                | otherwise = esDivisible (m - n) n

-- Ej 4. Especificar e implementar la funcion sumaImpares :: Integer -> Integer que dado n ∈ N sume los primeros n numeros impares

sumaImpares :: Integer -> Integer
-- requiere: x > 0, x mod 2 = 1, ó y = 2x+1
sumaImpares x | (x `mod` 2 == 0) = 0
              | x == 1 = 1
              | otherwise = x + sumaImpares(x-2)

-- Ej 5. Implementar la funcion medioFact :: Integer -> Integer que dado n ∈ N calcula n!! = n (n−2)(n−4)

medioFact :: Integer -> Integer
medioFact x | (x == 0 || x == 1) = 1
            | x > 0 = x * medioFact(x - 2)

-- Ej 6. Especificar e implementar la funcion sumaDigitos :: Integer ->Integer que calcula la suma de digitos de
-- un numero natural. Para esta funcion pueden utilizar div y mod.

sumaDigitos :: Integer -> Integer
sumaDigitos 0 = 0
sumaDigitos n = mod n 10 + sumaDigitos (div n 10)

-- Ej 7. Implementar la funcion todosDigitosIguales :: Integer -> Bool que determina si todos los digitos de un 
-- numero natural son iguales

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n > 0 && n < 10 = True
                      | otherwise = ultimoDigito n + primerDigito n + digitosMedio n