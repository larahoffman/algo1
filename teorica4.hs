f4 x y z | x == y = z
         | x ** y == y = x
         | otherwise = y
-- f4 5 5 True -> error

f5 x y z | x == y = z
         | x ** y == y = z
         | otherwise = z
-- f5 5 5 True -> True