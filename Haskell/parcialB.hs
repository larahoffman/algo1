-- Ejercicio 1
generarStock :: [[Char]] -> [([Char], Int)]
generarStock [] = []
generarStock (x:xs) = (x, 1 + cantidadApariciones x xs) : generarStock (quitarTodos x (x:xs))

cantidadApariciones :: [Char] -> [[Char]] -> Int
cantidadApariciones _ [] = 0
cantidadApariciones x (y:ys) | x == y = 1 + cantidadApariciones x ys
                             | otherwise = cantidadApariciones x ys

quitarTodos :: [Char] -> [[Char]] -> [[Char]]
quitarTodos _ [] = []
quitarTodos x (y:ys) | x == y = quitarTodos x ys
                     | otherwise = y : quitarTodos x ys

-- Ejercicio 2
stockDeProducto :: [([Char],Integer)] -> [Char] -> Integer
stockDeProducto [] _ = 0
stockDeProducto ((p,n):xs) producto | p == producto = n
                                    |otherwise = stockDeProducto xs producto

-- Ejercicio 3
dineroEnStock :: [([Char],Integer)] -> [([Char], Float)] -> Float
dineroEnStock [] _ = 0
dineroEnStock ((p,n):xs) precios = precioTotal (p,n) precios + dineroEnStock xs precios

precioTotal :: ([Char],Integer) -> [([Char], Float)] -> Float
precioTotal (p,n) ((producto, precio): xs) | p == producto = (fromIntegral n) * precio
                                           | otherwise = precioTotal (p,n) xs

-- Ejercicio 4
