--1
enumFromToo' :: Int -> Int -> [Int]
enumFromToo' x y = if x <= y then x : enumFromToo' (x+1) y
                 else []

--2
enumFromThenToo' :: Int -> Int -> Int -> [Int]
enumFromThenToo' x y z | x > y && y < z = []
                       | x > y && y > z = [x,y]
                       | x < y && y > z = [x]
enumFromThenToo' x y z = x : enumFromThenToo' (x+ k) (y +k) z
    where k = y-x

--3
concatenar :: [a] -> [a] -> [a]
concatenar [] l = l
concatenar l [] = l 
concatenar (h:t) l = h : concatenar t l

--4
posicao :: [a] -> Int -> a
posicao (h:t) 0 = h
posicao (h:t) x = posicao t (x-1)

--5
reversee' :: [a] -> [a]
reversee' [] = []
reversee' (h:t) = reversee' t ++ [h]

--6
takee' :: Int -> [a] -> [a]
takee' 0 _ = []
takee' _ [] = []
takee' x (h:t) = if x > 0 then h : takee' (x-1) t
               else []

--7
drop' :: Int -> [a] -> [a]
drop' 0 l = l
drop' _ [] = []
drop' x (h:t) = if (x >= length(h:t) || x < 0) then []
               else drop' (x-1) t

--8
zipp' :: [a] -> [b] -> [(a,b)]
zipp' _ [] = []
zipp' [] _ = []
zipp' (h:t) (x:y) = (h,x) : zipp' t y

--9
replicatee' :: Int -> a -> [a]
replicatee' x n = if x > 0 then n : replicatee' (x-1) n
                else []

--10
intersperse' :: a -> [a] -> [a]
intersperse' _ [] = []
intersperse' n [x] = [x]
intersperse' n (h:t) = h : n : intersperse' n t 

--11 
group' :: Eq a => [a] -> [[a]]
group' [] = []
group' (h:t) = takewhile' h (h:t) : group' (dropwhile' h (h:t))

takewhile' :: Eq a => a -> [a] -> [a]
takewhile' _ [] = []
takewhile' x (h:t) = if x == h then h : takewhile' x t
                     else []

dropwhile' :: Eq a => a -> [a] -> [a]
dropwhile' _ [] = []
dropwhile' x (h:t) = if x == h then dropwhile' x t
                     else (h:t)

--12
concatt' :: [[a]] -> [a]
concatt' [] = []
concatt' (h:t) = h ++ concatt' t

--13
inits' :: [a] -> [[a]]
inits' [] = [[]]
inits' l = inits'(retiraUltimo l) ++ [l] 

retiraUltimo :: [a] -> [a]
retiraUltimo [x] = []
retiraUltimo (h:t) = h : retiraUltimo t

--14
tails' :: [a] -> [[a]]
tails' [] = [[]]
tails' (h:t) = [(h:t)] ++ tails' t

--15
heads' :: [[a]] -> [a]
heads' [] = []
heads' ([]:t) = heads' t
heads' ((x:xs):t) = x : heads' t

--16
total' :: [[a]] -> Int
total' [] = 0
total' (x:xs) = length x + total' xs

--17
fun' :: [(a,b,c)] -> [(a,c)]
fun' [] = []
fun' ((a,b,c):t) = (a,c) : fun' t

--18
cola :: [(String, b, c)] -> String
cola [] = []
cola ((a,b,c):xs) = a ++ cola xs

--19
idade :: Int -> Int -> [(String, Int)] -> [String]
idade _ _ [] = []
idade x y ((a,b):xs) = if x-b >= y then a : idade x y xs
                       else idade x y xs

--20
powerEnumFrom :: Int -> Int -> [Int] 
powerEnumFrom n m = aux n m 0

aux :: Int -> Int -> Int -> [Int]
aux n m acc = if acc /= m then n^acc : aux n m (acc+1)
              else []

--21
isPrime :: Int -> Bool
isPrime 1 = False
isPrime x = if numeroDeDivisores x 2 == 0 then True
            else False

numeroDeDivisores :: Int -> Int -> Int
numeroDeDivisores x y | y >= x = 0
                      | mod x y == 0 = 1
                      | otherwise = numeroDeDivisores x (y+1) 

--22
isPrefixOf' :: Eq a => [a] -> [a] -> Bool
isPrefixOf' [] l = True
isPrefixOf' (x:xs) (h:t) = if x == h then isPrefixOf' xs t
                          else False

--23
isSuffixOf' :: Eq a => [a] -> [a] -> Bool
isSuffixOf' [] [] = True
isSuffixOf' l [] = False
isSuffixOf' (x:xs) (h:t) = if x == h then isSuffixOf' xs t
                          else isSuffixOf' (x:xs) t


--24
isSubsequenceOf' :: Eq a => [a] -> [a] -> Bool
isSubsequenceOf' [] l = True
isSubsequenceOf' l []  = False
isSubsequenceOf' (x:xs) (h:t) = if x == h then isSubsequenceOf' xs t
                               else isSubsequenceOf' (x:xs) t

--25
elemIndices :: Eq a => a -> [a] -> [Int]
elemIndices x [] = []
elemIndices x l = aux' x l 0

aux' :: Eq a => a -> [a] -> Int -> [Int]
aux' _ [] _ = []
aux' x (h:t) n = if x == h then n : aux' x t (n+1)
                else aux' x t (n+1)

--26
nub' :: Eq a => [a] -> [a]
nub' [] = []
nub' (h:t) = if pertence h t then nub' t
            else h : nub' t

pertence :: Eq a => a -> [a] -> Bool
pertence x [] = False
pertence x (h:t) = if x == h then True
                   else pertence x t

--27
delete' :: Eq a => a -> [a] -> [a]
delete' _ [] = []
delete' x (h:h2:t) | x == h = h2:t
                   | x == h2 = h:t
                   |otherwise = delete' x t
-- ou então
delete2 :: Eq a => a -> [a] -> [a]
delete2 _ [] = []
delete2 x (h:t) = if x == h then t
                  else h: delete2 x t

--28
barra :: Eq a => [a] -> [a] -> [a]
barra [] _ = []
barra l [] = l
barra (h:t) (x:xs) = barra (delete2 x (h:t)) xs

--29
uniao :: Eq a => [a] -> [a] -> [a]
uniao [] l = l
uniao l [] = l
uniao (x:xs) (h:t) = if pertence x (h:t) then uniao (h:t) xs
                     else x : uniao xs (h:t)

--30
intersect :: Eq a => [a] -> [a] -> [a]
intersect l [] = []
intersect [] l = []
intersect (h:t) (x:xs) = if pertence h (x:xs) then h : intersect t (x:xs)
                         else intersect t (x:xs)

--31
insert' :: Ord a => a -> [a] -> [a]
insert' x [] = [x]
insert' x (h:t) = if x <= h then x:h:t
                 else h : insert' x t

--32
unwordss' :: [String] -> String
unwordss' [] = []
unwordss' [x] = x
unwordss' (h:t) = h ++ " " ++ unwordss' t

--33
unliness' :: [String] -> String
unliness' [] = []
unliness' (h:t) = h ++ "\n" ++ unliness' t

--34
pMaior :: Ord a => [a] -> Int
pMaior (h:t) = aux3 h t 0 1

aux3 :: Ord a => a -> [a] -> Int -> Int -> Int
aux3 _ [] x _ = x
aux3 m (h:t) x n = if h > m then aux3 h t n (n+1)
                   else aux3 m t x (n+1)

--35
lookupp' :: Eq a => a -> [(a,b)] -> Maybe b
lookupp' _ [] = Nothing
lookupp' x ((a,b):t) = if x == a then Just b
                       else lookupp' x t

--36
preCrescente :: Ord a => [a] -> [a]
preCrescente [] = []
preCrescente [x] = [x]
preCrescente (x:y:t) = if x <= y then x : preCrescente(y:t)
                       else [x]

--37
iSortt :: Ord a => [a] -> [a]
iSortt [] = []
iSortt (h:t) = insert2 h (iSortt t)

insert2 :: Ord a => a -> [a] -> [a]
insert2 x [] = [x]
insert2 x (h:t) = if x <= h then x:h:t
                  else h : insert2 x t

--38
menor :: String -> String -> Bool
menor [] [] = True
menor l [] = False
menor [] l = True
menor (x:xs) (h:t) | x < h =  True
                   | x > h = False
                   | otherwise = menor xs t

--39
elemMSet :: Eq a => a -> [(a,Int)] -> Bool
elemMSet _ [] =  False
elemMSet x ((a,b):t) = if x == a then True
                       else elemMSet x t

--40
converteMSet :: [(a,Int)] -> [a]
converteMSet [] = []
converteMSet ((a,b):t) = if b > 0 then a : converteMSet((a,b-1):t)
                         else converteMSet t

--41
insereMSet :: Eq a => a -> [(a,Int)] -> [(a, Int)]
insereMSet x [] = [(x,1)]
insereMSet x ((a,b):t) = if x == a then (a,b+1):t
                         else (a,b) : insereMSet x t

--42
removeMSet :: Eq a => a -> [(a,Int)] -> [(a,Int)]
removeMSet x [] = []
removeMSet x ((a,b):t) | x == a && b == 1 = t
                       | x == a = (a,b-1):t
                       | otherwise = (a,b) : removeMSet x t

--43 há formas muito mais eficientes de fazer isto
constroiMSet :: Ord a => [a] -> [(a,Int)]
constroiMSet [] = []
constroiMSet (h:t) = auxVersao19mil h 1 t : constroiMSet (dropwhile'' h t)

auxVersao19mil :: Ord a => a -> Int -> [a] -> (a, Int)
auxVersao19mil h n [] = (h,n)
auxVersao19mil h n (x:xs) = if h == x then auxVersao19mil h (n+1) xs
                            else (h,n)

dropwhile'' :: Eq a => a -> [a] -> [a]
dropwhile'' h [] = []
dropwhile'' h (x:xs) = if (h == x) then dropwhile'' h xs
                       else (x:xs)

--44
partitionEitherss :: [Either a b] -> ([a], [b])
partitionEitherss [] = ([],[])
partitionEitherss (h:t) = case h of
        Left a -> (a:x , y)
        Right b -> (x , b:y )
    where (x,y) = partitionEitherss t

--45
catMaybes' :: [Maybe a] -> [a]
catMaybes' [] = []
catMaybes' (h:t) = case h of
    Just a -> a : catMaybes' t
    Nothing -> catMaybes' t

--46
data Movimento = Norte | Sul | Este | Oeste
               deriving Show

caminho :: (Int, Int) -> (Int, Int) -> [Movimento]
caminho (x,y) (x2,y2) | x > x2 = Oeste : caminho (x-1,y) (x2,y2)
                      | x < x2 = Este : caminho (x+1, y) (x2,y2)
                      | y > y2 = Sul : caminho (x, y-1) (x2,y2)
                      | y < y2 = Norte : caminho (x, y+1) (x2,y2)
                      | otherwise = []

--47 que feio, tentar otimizar
hasLoops :: (Int, Int) -> [Movimento] -> Bool
hasLoops (x,y) [] = False
hasLoops (x,y) (h:t) = case h of
    Norte -> aux'' (x,y) (x,y+1) t
    Sul -> aux'' (x,y) (x,y-1) t
    Este -> aux'' (x,y) (x+1,y) t
    Oeste -> aux'' (x,y) (x-1, y) t 

aux'' :: (Int, Int) -> (Int, Int) -> [Movimento] -> Bool
-- (xi,yi) x inicial y inicial   ...  (xa,ya) x atual y atual
aux'' (xi, yi) (xa, ya) [] = if xi == xa && yi == ya then True
                             else False
aux'' (xi, yi) (xa,ya) (h:t) = if xi == xa && yi == ya then True
                               else case h of
                                   Norte -> aux'' (xi,yi) (xa,ya+1) t
                                   Sul -> aux'' (xi,yi) (xa,ya-1) t
                                   Oeste -> aux'' (xi,yi) (xa-1,ya) t
                                   Este -> aux'' (xi,yi) (xa+1, ya) t

--48
type Ponto = (Float,Float)
data Rectangulo = Rect Ponto Ponto

contaQuadrados :: [Rectangulo] -> Int 
contaQuadrados [] = 0
contaQuadrados ((Rect (x1,y1) (x2,y2)):t) = if abs(x1-x2) == abs(y1-y2) then 1 + contaQuadrados t
                                            else contaQuadrados t


--49
areaTotal :: [Rectangulo] -> Float
areaTotal [] = 0
areaTotal ((Rect (x1,y1) (x2,y2)):t) = abs(x1-x2) * abs(y1-y2) + areaTotal t

--50
data Equipamento = Bom | Razoavel | Avariado
                 deriving Show

naoReparar :: [Equipamento] -> Int
naoReparar [] = 0
naoReparar (h:t) = case h of
    Avariado -> naoReparar t
    _ -> 1 + naoReparar t