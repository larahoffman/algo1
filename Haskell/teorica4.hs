f4 x y z | x == y = z
         | x ** y == y = x
         | otherwise = y
-- f4 5 5 True -> error

f5 x y z | x == y = z
         | x ** y == y = z
         | otherwise = z
-- f5 5 5 True -> True

-- para el otro archivo


--ejer 1
fibonacci:: Integer ->Integer
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | otherwise = fibonacci(n-1) + fibonacci(n-2)

--Ej 2--
parteEntera :: Float ->Integer
parteEntera n | n < 1 && n > 0 = 0
              | n > -1 && n <= 0 = -1 
              | n >= -1 = 1 + parteEntera(n-1)
              | otherwise = -1 + parteEntera(n+1)

--EJ 3--
esDivisible :: Integer ->Integer ->Bool
esDivisible n m | n < m = False
                | n == m = True
                | otherwise = esDivisible(n-m) m

--EJ 4--
sumaImpares :: Integer ->Integer
sumaImpares n = contarSuma (1) (n)

contarSuma :: Integer ->Integer ->Integer
contarSuma num cant | cant == 0 = 0
                    | otherwise = num + contarSuma (num + 2) (cant - 1)


--Ej 5--
medioFact :: Integer ->Integer
medioFact n | n == 0 = 1
            | otherwise = n * (medioFact(n-2))

--EJ 6--

sumaDigitos :: Integer ->Integer
sumaDigitos n | n == 0 = 0
              | otherwise = mod n 10 + sumaDigitos (div n 10)

--EJ 7 --

todosDigitosIguales :: Integer ->Bool
todosDigitosIguales n | n < 10 = True
                      | otherwise = ultimoDigito(n) == ultimoDigito(sacarUltimoDigito(n)) && todosDigitosIguales(sacarUltimoDigito(n))


ultimoDigito :: Integer -> Integer
ultimoDigito n = mod n 10

sacarUltimoDigito :: Integer -> Integer
sacarUltimoDigito n = div n 10

sacarPrimerDigito :: Integer -> Integer
sacarPrimerDigito n = mod n (10 ^ ((cantDigitos n) - 1))

reducirNumero :: Integer -> Integer
reducirNumero n = sacarPrimerDigito (sacarUltimoDigito (n))
--EJ 8--
iesimoDigito :: Integer ->Integer ->Integer
iesimoDigito n i = mod (div n (10 ^ ((cantDigitos n) - i))) 10


cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
              | otherwise = 1 + cantDigitos(sacarUltimoDigito(n))

--EJ 9 --
esCapicua :: Integer ->Bool
esCapicua n | n < 10 = True
            | otherwise = iesimoDigito n 1 == iesimoDigito n (cantDigitos(n)) &&  esCapicua(reducirNumero(n))

--ej 10 A--
f1 :: Integer -> Integer 
f1 n | n == 0 = 1
     | otherwise = (2^n) + f1(n-1) 
--EJ 10 B--
f2 :: Integer -> Integer -> Integer 
f2 n q | n == 1 = q
       | otherwise = (q^n) + f2(n-1) q

--EJ 10 C--
f3 :: Integer -> Integer -> Integer
f3 n q = f2 (2*n) q

--EJ 10 D--
f4 :: Integer -> Integer -> Integer
f4 n q = f4Aux n (2*n) q

f4Aux :: Integer -> Integer -> Integer -> Integer
f4Aux i n q | i == n = q^i 
            | otherwise = q^i + f4Aux (i+1) n q  

--EJ 11--
esAprox :: Integer ->Float
esAprox e | e == 0 = 1 
         | otherwise = (1/factorial(e)) + esAprox(e-1)
 
factorial :: Integer -> Float
factorial n | n == 0 = 1
            | otherwise = fromIntegral n * factorial(n-1)

--b--
e :: Float
e = esAprox 10

--EJ 11--
raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = aprox n - 1

aprox :: Integer ->Float
aprox n | n == 1 = 2
        |  otherwise = 2 + (1/aprox(n-1))

--EJ 13--

sumatoria :: Integer -> Integer -> Integer
sumatoria i j | i==1 = sumatoriaAux 1 j 
      | otherwise = sumatoriaAux i j + sumatoria(i-1) j

sumatoriaAux :: Integer -> Integer -> Integer
sumatoriaAux i j | j == 1 = i 
                 | otherwise = i^j + sumatoriaAux i (j-1)

--EJ 14--

sumaPotencias :: Integer ->Integer ->Integer ->Integer
sumaPotencias q n m | n == 1 = sumaAux q 1 m
                    | otherwise = sumaAux q n m + sumaPotencias q (n-1) m

sumaAux :: Integer -> Integer -> Integer -> Integer
sumaAux q n m | m == 1 = q^(n+1)
              | otherwise = q^(n+m) + sumaAux q n (m-1)

--EJ 15

sumaRacionales :: Integer ->Integer ->Float
sumaRacionales p q | p == 1 = racionalesAux 1 q
                   | otherwise = racionalesAux p q + sumaRacionales (p-1) q
racionalesAux :: Integer -> Integer -> Float
racionalesAux p q | q == 1 = fromIntegral p
                  | otherwise = (fromIntegral p)/(fromIntegral q) + racionalesAux p (q-1)


--EJ 16--
--A--
menorDivisor :: Integer ->Integer
menorDivisor n = menorDivisorAux n 2 

menorDivisorAux :: Integer -> Integer ->Integer
menorDivisorAux n i | n == i = n
                    | esDivisible n i = i
                    | otherwise = menorDivisorAux n (i+1)

--B--
esPrimo :: Integer ->Bool
esPrimo n | n == 1 = False
          | menorDivisor n == n = True
          | otherwise = False

--C--

sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos n m = coprimosAux n m 2

coprimosAux :: Integer -> Integer -> Integer -> Bool
coprimosAux n m divisor | divisor > n || divisor > m = True
                         | (esDivisible n divisor) && (esDivisible m divisor) = False
                         | otherwise = coprimosAux n m (divisor + 1)

--D--

nEsimoPrimo :: Integer ->Integer
nEsimoPrimo n = nEsimoPrimoAux n 0 2

nEsimoPrimoAux :: Integer -> Integer -> Integer -> Integer
nEsimoPrimoAux n cont aux | esPrimo aux && cont == n-1 = aux
                          | esPrimo aux = nEsimoPrimoAux n (cont+1) (aux+1)
                          | otherwise = nEsimoPrimoAux n cont (aux+1)

--17--
esFibonacci :: Integer -> Bool
esFibonacci n = esFibonacciAux n 0

esFibonacciAux :: Integer -> Integer -> Bool
esFibonacciAux n cont | n == fibonacci cont = True
           | fibonacci cont > n = False
           | otherwise = esFibonacciAux n (cont+1)


--18--

mayorDigitoPar :: Int -> Int
mayorDigitoPar n = mayorDigitoParAux n (-1)

mayorDigitoParAux :: Int -> Int -> Int
mayorDigitoParAux n max | n == 0 = max
                        | esPar (digito n) && digito n > max = mayorDigitoParAux (sacarUltimo n) (digito n)
                        | otherwise = mayorDigitoParAux (sacarUltimo n) max 

esPar :: Int -> Bool
esPar n = mod n 2 == 0

sacarUltimo :: Int -> Int
sacarUltimo n = div n 10 

digito :: Int -> Int
digito n = mod n 10

--19--
esSumaInicialDePrimos :: Integer ->Bool
esSumaInicialDePrimos n = esSumaInicialDePrimosAux n 2

esSumaInicialDePrimosAux :: Integer -> Integer -> Bool
esSumaInicialDePrimosAux n q | n == sumaPrimosHasta 2 q = True
                             | n < sumaPrimosHasta 2 q = False
                             | otherwise = esSumaInicialDePrimosAux n (q+1)

sumaPrimosHasta :: Integer -> Integer -> Integer
sumaPrimosHasta m n  | esPrimo n && n == m = m
                     | n == m = 0
                     | esPrimo m = m + sumaPrimosHasta (m + 1) n
                     | otherwise = sumaPrimosHasta (m+1) n


--20--

tomaValorMax :: Integer -> Integer -> Integer 
tomaValorMax n1 n2 = tomaValorMaxAux n1 n2 0

tomaValorMaxAux :: Integer -> Integer -> Integer -> Integer 
tomaValorMaxAux n1 n2 max | n1 == n2 && sumaDivisores n1 > max = sumaDivisores n1 
                          | n1 == n2 = max 
                          | sumaDivisores n1 > max = tomaValorMaxAux (n1+1) n2 (sumaDivisores n1)
                          | otherwise = tomaValorMaxAux (n1+1) n2 max 

sumaDivisores :: Integer -> Integer
sumaDivisores n = sumaDivisoresAux n 1 

sumaDivisoresAux :: Integer -> Integer -> Integer
sumaDivisoresAux n divisor | divisor == n = divisor 
                           | esDivisible divisor n = divisor + sumaDivisoresAux n (divisor + 1)
                           | otherwise = sumaDivisoresAux n (divisor + 1)
