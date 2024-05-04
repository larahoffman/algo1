-- Ej 1.

longitud :: [t] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs) | longitud(xs) > 0 = ultimo xs

eliminarNumero :: (Eq t) => [t] -> t -> [t]
eliminarNumero [] _ = []
eliminarNumero (x:xs) y | x == y = eliminarNumero xs y
                        | otherwise = x : eliminarNumero xs y

principio :: (Eq t) => [t] -> [t]
principio [x] = [x]
principio (x:xs) = eliminarNumero (x:xs) (ultimo xs)

reverso :: (Eq t) => [t] -> [t]
reverso [] = []
reverso [x] = [x]
reverso (x:xs) = ultimo xs : reverso (eliminarNumero (x:xs) (ultimo xs))

-- Ej 2.

-- Ej 2.1
pertenece :: (Eq t) => t -> [t] -> Bool -- defino/agrego la función igualdad Eq
pertenece x [] = False
pertenece x (y:ys)| x == y = True
                  | otherwise = pertenece x ys

-- Ej 2.2. Dada una lista devuelve verdadero si y solamente si todos sus elementos son iguales. 
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [x] = True
todosIguales (x:xs) = x == head xs && todosIguales xs

-- Ej 2.3 El resultado es falso si existen dos posiciones distintas de s con igual valor
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos [x] = True
todosDistintos (x:xs) | pertenece x xs = False
                      | otherwise = todosDistintos xs

-- Ej 2.4
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (y:ys) | pertenece y ys = True
                    | otherwise = hayRepetidos ys

-- Ej 2.5
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar x (y:ys) | x == y = ys
                | otherwise = y : quitar x ys

-- Ej 2.6 
quitarTodos ::  (Eq t ) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos x (y:ys) | x == y = quitarTodos x ys
                     | otherwise = y : quitarTodos x ys

-- Ej 2.7. Deja en la lista una unica aparicion de cada elemento, eliminando las repeticiones adicionales.
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x : eliminarRepetidos(quitarTodos x xs)

-- Ej 2.8. Dadas dos listas devuelve verdadero si y solamente si ambas listas contienen los mismos elementos, sin tener en cuenta repeticiones
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] [] = True
mismosElementos xs ys = estaContenida xs ys && estaContenida ys xs

estaContenida :: (Eq t) => [t] -> [t] -> Bool
estaContenida [] ys = True
estaContenida (x:xs) ys = pertenece x ys && estaContenida xs ys

-- Ej 2.9
capicua :: (Eq t) => [t] -> Bool
capicua [] = True
capicua xs = xs == reverso xs

-- Ej 3

-- Ej 3.1

sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

-- Ej 3.2
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs

-- Ej 3.3
maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:ys) | x >= y = maximo (x:ys)
                | otherwise = maximo (y:ys)

-- Ej 3.4 cada posicion de resultado contiene el valor que hay en esa posicion en s sumado n
sumarN ::  Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:xs) = (x+n) : sumarN n xs

-- Ej 3.5
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs)

-- Ej 3.6
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs)

-- Ej 3.7
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | esPar x = x : pares xs
             | otherwise = pares xs

esPar :: Integer -> Bool
esPar n = mod n 2 == 0

-- Ej 3.8 Dado un numero n y una lista xs, devuelve una lista con los elementos de xs multiplos de n
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs) | esMultiplo x n = x : multiplosDeN n xs
                      | otherwise = multiplosDeN n xs

esMultiplo :: Integer -> Integer -> Bool
esMultiplo x n = mod x n == 0

-- Ej 3.9 ordena los elementos de la lista en forma creciente
ordenar :: [Int] -> [Int]
ordenar [] = []
ordenar xs = ordenar ((quitar (maximo xs) xs)) ++ maximo xs : []

-- Ej 4. Palabra = secuencia de caracteres sin blancos

-- Ej 4.a. Reemplaza cada subsecuencia de blancos contiguos de la primera lista por un solo blanco en la lista resultado
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x:[]) = [x]
sacarBlancosRepetidos (x:y:ys) | x == y && y == ' ' = sacarBlancosRepetidos (x:ys)
                             | otherwise = x : sacarBlancosRepetidos (y:ys)