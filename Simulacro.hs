-- Simulacro

-- Ej 1. El resultado es verdadero si relaciones no contiene ni tuplas repetidas1, ni tuplas con ambas componentes iguales
-- dos tuplas son iguales si el par de elementos que las componen (sin importar el orden) son iguales
relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas (x:xs) = not(ambasIguales x) && not(hayTuplasRepetidas x xs) && relacionesValidas xs

hayTuplasRepetidas :: (String, String) -> [(String, String)] -> Bool
hayTuplasRepetidas _ [] = False
hayTuplasRepetidas (a,b) (x:xs) | (((a == fst x ) && (b == snd x)) || ((a == snd x) && (b == fst x))) = True
                                | otherwise = hayTuplasRepetidas (a,b) xs

ambasIguales :: (String, String) -> Bool
ambasIguales (a,b) = a == b

-- Ej 2.
personas :: [(String, String)] -> [String]
personas [] = []
personas (x:xs) = eliminarRepetidos (personasRepetidas (x:xs))

eliminarRepetidos :: [String] -> [String]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x : eliminarRepetidos (quitarTodos x xs)

quitarTodos :: String -> [String] -> [String]
quitarTodos _ [] = []
quitarTodos x (y:ys) | x == y = quitarTodos x ys
                     | otherwise = y : quitarTodos x ys

personasRepetidas :: [(String, String)] -> [String]
personasRepetidas [] = []
personasRepetidas (x:xs) = (fst x) : (snd x) : (personasRepetidas xs)

-- Ej 3 res tiene exactamente los elementos que figuran en las tuplas de relaciones en las que una de sus componentes es persona
amigosDe :: String -> [(String, String)] -> [String]
amigosDe _ [] = []
amigosDe x ((y1,y2):ys) | x == y1 = y2 : (amigosDe x ys)
                        | x == y2 = y1 : (amigosDe x ys)
                        | otherwise = amigosDe x ys

-- Ej 4
personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos [x] = fst x
personaConMasAmigos ((x1,x2):xs) | longitud (amigosDe x1 ((x1,x2):xs)) > longitud (amigosDe x2 ((x1,x2):xs)) = x1
                                 | longitud (amigosDe x1 ((x1,x2):xs)) < longitud (amigosDe x2 ((x1,x2):xs)) = x2
                                 | otherwise = personaConMasAmigos xs
longitud :: [t] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs
