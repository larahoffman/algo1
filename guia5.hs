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

principio :: [t] -> [t]
principio [x] = [x]
principio (x:xs:xss) | longitud(x:xs:xss) > 0 = principio (x:[])
-- no se si estan pidiendo eso

reverso :: [t] -> [t]
reverso [] = []
reverso [x] = [x]
reverso (x:xs) = reverso(principio(ultimo xs :[])) -- faltaria un concat
