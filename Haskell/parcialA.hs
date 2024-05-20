-- Ej 1
hayQueCodificar :: Char -> [(Char, Char)] -> Bool
hayQueCodificar _ [] = False
hayQueCodificar c ((y1,y2):ys) | c == y1 = True
                               | otherwise = hayQueCodificar c ys

-- Ej 2
cuantasVecesHayQueCodificar :: Char -> [Char] -> [(Char, Char)] -> Int
cuantasVecesHayQueCodificar c frase mapeo | (hayQueCodificar c mapeo) == False = 0
                                          | otherwise = cantidadApariciones c frase

cantidadApariciones :: Char -> [Char] -> Int
cantidadApariciones _ [] = 0
cantidadApariciones c (f1:f2) | c == f1 = 1 + cantidadApariciones c f2
                              | otherwise = cantidadApariciones c f2

-- Ej 3
laQueMasHayQueCodificar :: [Char] -> [(Char, Char)] -> Char
laQueMasHayQueCodificar frase mapeo = laQueMasHayQueCodificarAux frase frase mapeo

laQueMasHayQueCodificarAux :: [Char] -> [Char] -> [(Char, Char)] -> Char
laQueMasHayQueCodificarAux [f] _ _ = f
laQueMasHayQueCodificarAux (f1:f2:fs) fraseOriginal mapeo
    | f1 == f2 = laQueMasHayQueCodificarAux (f1:fs) fraseOriginal mapeo
    | cuantasVecesHayQueCodificar f1 fraseOriginal mapeo >= cuantasVecesHayQueCodificar f2 fraseOriginal mapeo = laQueMasHayQueCodificarAux (f1:fs) fraseOriginal mapeo
    | otherwise = laQueMasHayQueCodificarAux (f2:fs) fraseOriginal mapeo

-- Ej 4
--codificarFrase :: [Char] -> [(Char, Char)] -> [Char]
--
