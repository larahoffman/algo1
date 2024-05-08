-- Ej 1
aproboMasDeNMaterias :: [([Char], [Int])] -> [Char] -> Int -> Bool
aproboMasDeNMaterias registro alumno n = ((aproboMasDeNMateriasAux registro alumno) > n)

aproboMasDeNMateriasAux :: [([Char], [Int])] -> [Char] -> Int
aproboMasDeNMateriasAux ((alum, notas):xs) alumno | alumno == alum = cantidadMateriasAprobadas notas
                                                  | otherwise = aproboMasDeNMateriasAux xs alumno

cantidadMateriasAprobadas :: [Int] -> Int
cantidadMateriasAprobadas [] = 0
cantidadMateriasAprobadas (n1:notas) | n1 >= 4 = 1 + cantidadMateriasAprobadas notas
                                     | otherwise = cantidadMateriasAprobadas notas

-- Ej 2
buenosAlumnos :: [([Char], [Int])] -> [[Char]]
buenosAlumnos registro = buenosAlumnosAux registro