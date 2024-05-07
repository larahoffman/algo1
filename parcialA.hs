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