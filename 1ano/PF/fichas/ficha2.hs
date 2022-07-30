--2 
--a
dobros :: [Float] -> [Float]
dobros [] = []
dobros (h:t) = 2*h : dobros t

--b
numOcorre :: Char -> String -> Int
numOcorre x [] = 0
numOcorre x (h:t) = if x == h then 1 + numOcorre x t
                    else numOcorre x t

--c
positivos :: [Int] -> Bool
positivos [] = True
positivos (h:t) = if h < 0 then False
                  else positivos t

--d
soPos :: [Int] -> [Int]
soPos [] = []
soPos (h:t) = if h > 0 then h : soPos t
              else soPos t

--e
somaNeg :: [Int] -> Int
somaNeg [] = 0
somaNeg (h:t) = if h < 0 then h + somaNeg t
                else somaNeg t

--f
tresUlt :: [a] -> [a]
tresUlt [] = []
tresUlt (h:t) = if length((h:t)) <= 3 then (h:t)
            else tresUlt t

--g
segundos :: [(a,b)] -> [b]
segundos [] = []
segundos ((a,b):t) = b : segundos t

--h
nosPrimeiros :: (Eq a) => a -> [(a,b)] -> Bool
nosPrimeiros _ [] = False
nosPrimeiros x ((a,b):t) = if x == a then True
                           else nosPrimeiros x t 

--i
sumTriplos :: (Num a, Num b, Num c) => [(a,b,c)] -> (a,b,c)
sumTriplos [] = (0,0,0)
sumTriplos ((a,b,c):t) = (a+ somaA, b+ somaB, c+ somaC)
    where (somaA, somaB, somaC) = sumTriplos t

--4
type Polinomio = [Monomio]
type Monomio = (Float, Int)

--a
conta :: Int -> Polinomio -> Int
conta n [] = 0
conta n ((a,x):t) = if n == x then  1+ conta n t
                    else conta n t

--b
grau :: Polinomio -> Int
grau [(a,x1)] = x1 
grau ((a,x1):(b,x2):t) = if x1 >= x2 then grau((a,x1):t)
                         else grau((b,x2):t)

--c
selgrau :: Int -> Polinomio -> Polinomio
selgrau _ [] = []
selgrau n ((a,x):t) = if n == x then (a,x): selgrau n t
                      else selgrau n t

--d
deriv :: Polinomio -> Polinomio
deriv [] = []
deriv((a,0):t) = deriv t
deriv ((a,x):t) = (a*fromIntegral(x), x-1): deriv t

--e
calcula :: Float -> Polinomio -> Float
calcula x [] = 0
calcula x ((a,n):t) = a*(x^n) + calcula x t

--f
simp :: Polinomio -> Polinomio
simp [] = []
simp ((a,n):t) | a == 0 = simp t
               | otherwise = (a,n) : simp t

--g
mult :: Monomio -> Polinomio -> Polinomio
mult _ [] = []
mult (x1,n) ((x2,k):t) = (x1*x2, n+k) : mult (x1,n) t

--h
normaliza :: Polinomio -> Polinomio
normaliza [] = []
normaliza [(b,e)] = [(b,e)]
normaliza ((b, e) : (b2, e2) : ps) | e == e2 = normaliza ((b + b2, e) : ps)
                                   | conta e ps == 0 = (b, e) : normaliza ((b2, e2) : ps)
                                   | otherwise = normaliza ((b, e) : ps ++ [(b2, e2)])

--i
soma :: Polinomio -> Polinomio -> Polinomio
soma [] l = l
soma l [] = l
soma p1 p2 = normaliza (p1 ++ p2)

--j
produto :: Polinomio -> Polinomio -> Polinomio
produto [] p = []
produto p [] = []
produto (h:t) (x:xs) = soma (mult h (x:xs)) (produto t (x:xs))

--k
ordena :: Polinomio -> Polinomio
ordena [] = []
ordena ((a,x):t) = insere (a,x) (ordena t)
    where insere (a,x) [] = (a,x)
          insere (a,x1) ((b,x2):t) = if x1 <= x2 then ((a,x1):(b,x2):t)
                                     else (b,x2): insere (a,x1) t

--l
equiv :: Polinomio -> Polinomio -> Bool
equiv [] [] = True
equiv p1 p2 | ordena(normaliza p1) == ordena(normaliza p2) = True
            | otherwise = False