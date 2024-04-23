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
ordenar (e:x:xs)

-- Ej 3.9
ordenar :: [Int] -> [Int]
ordenar [] = []
ordenar xs = quitar (maximo xs) xs ++ maximo xs : [] -- incompleto
