-- Clase 22/04

-- Ej 2.1
pertenece :: (Eq t) => t -> [t] -> Bool -- defino/agrego la función igualdad Eq
pertenece x [] = False
pertenece x (y:ys)| x == y = True
                  | otherwise = pertenece x ys

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

-- Ej 3.3
maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:ys) | x >= y = maximo (x:ys)
                | otherwise = maximo (y:ys)


-- Ej 3.9
ordenar :: [Int] -> [Int]
ordenar [] = []
ordenar xs = ordenar ((quitar (maximo xs) xs)) ++ maximo xs : []

-- 
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
