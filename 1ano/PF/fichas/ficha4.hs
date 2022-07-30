import Data.Char

--1
digitAlpha :: String -> (String, String)
digitAlpha [] = ([],[])
digitAlpha (x:xs) | isAlpha x = (x: r1, r2)
                  | isDigit x = (r1, x:r2)
                  | otherwise = (r1,r2)
    where (r1,r2) = digitAlpha xs

--2
nzp :: [Int] -> (Int, Int, Int)
nzp [] = (0,0,0)
nzp (x:xs) | x == 0 = (a,1+b,c)
           | x > 0 = (1+a,b,c)
           | x < 0 = (a,b,1+c)
    where (a,b,c) = nzp xs

--3
divMod' :: Integral a => a -> a -> (a,a)
divMod' a 0 = error "Divisão por 0"
divMod' a b | a<0 && b>0 || a>0 && b<0 = (-res,resp)
            | (a-b)<=0 = (x,(y+a))
            | otherwise = ((x+1),y)
    where (x,y) = (divMod' (a-b) (b) )
          (res,resp) = (divMod' (abs a) (abs b))

--4
fromDigitss :: [Int] -> Int
fromDigitss [] = 0
fromDigitss (h:t) = aux t h

aux :: [Int] -> Int -> Int
aux [] acc = acc
aux (h:t) acc = aux t (h+ 10*acc)

--5
maxSumInit :: (Num a, Ord a) => [a] -> a
maxSumInit [] = 0
maxSumInit l = foldl (\acc x-> max acc (sum x)) 0 (inits l)

inits :: [a] -> [[a]]
inits [] = [[]]
inits l = inits (init l) ++ [l]

--6
fib :: Int -> Int
-- o 1 e o 2 são o primeiro e segundo termo da série
-- de Fibonacci, respetivamente
fib n = auxx n 1 1

auxx :: Int -> Int -> Int -> Int
-- o termo de paragem é 2 porque o meu n
auxx 1 acc1 _ = acc1
auxx n acc1 acc2 = auxx (n-1) (acc2) (acc2+acc1)

--7 fazer depois


--8
-- a)
-- [x | x <- [1..20], mod x 2 == 0, mod x 3 == 0]
-- divisores de 6 entre 1 e 20

-- b)
-- [x | x <- [y | y <- [1..20], mod y 2 == 0], mod x 3 == 0]
-- igual à alínea a)

-- c)
-- [(x,y) | x <- [0..20], y <- [0..20], x+y == 30]
-- pares (x,y) entre 1 e 20 cuja soma de x e y é igual a 30

-- d)
-- [sum [y | y <- [1..x], odd y] | x <- [1..10]]

--9
--a
[ 2^y | y <- [0..10]]

--b
[(x,y) | x <- [1..5] , y <- [1..5], x+y == 6]

--c

--d

--e
