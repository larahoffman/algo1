-- Ejercicio 1.a

f :: Integer -> Integer
f 1 = 8
f 131 = 4
f 16 = 16

-- Ejercicio 1.b

g :: Integer -> Integer
g 8 = 16
g 16 = 4
g 131 = 1

-- Ejercicio 1.c

h :: Integer -> Integer
h x = f (g x)

k :: Integer -> Integer
k y = g (f y)

-- Ejercicio 2

maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 x y z | x > y && x > z = x
              | y > z = y
              | otherwise = z

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | (x /= y) && (x /= z) && (y /= z) = x + y + z
                    | (x /= y) && (y == z) = x + y
                    | (y /= z) && (x == z) = y + x
                    | (x == y) && (x == z) && (y == z) = 0
                    | otherwise = y + z
digitoUnidades :: Integer -> Integer
digitoUnidades x | (x >= 0) && (x < 10) = x
                 | x >= 10 = mod x 10
                 | otherwise = (-x)

-- con la precondiciòn de que x >= 0
digitoUnidades2 :: Integer -> Integer
digitoUnidades2 x = mod x 10

digitoDecenas :: Integer -> Integer
digitoDecenas 10 = 1
digitoDecenas x = digitoDecenas(digitoUnidades x) -- algo así
