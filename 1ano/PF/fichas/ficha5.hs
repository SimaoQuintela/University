--1
--a
any' :: (a -> Bool) -> [a] -> Bool
any' f [] = False
any' f (h:t) = if f h then True
               else any' f t
--b
zipWithh :: (a->b->c) -> [a] -> [b] -> [c]
zipWithh _ _ [] = []
zipWithh _ [] _ = []
zipWithh f (h:t) (x:xs) = (f h x) : zipWithh f t xs
--c
takeWhilee :: (a->Bool) -> [a] -> [a]
takeWhilee _ [] = []
takeWhilee f (h:t) = if f h then h : takeWhilee f t
                     else []
--d
dropWhilee :: (a->Bool) -> [a] -> [a]
dropWhilee _ [] = []
dropWhilee f (h:t) = if f h then dropWhilee f t
                     else (h:t)

--e
spann :: (a -> Bool) -> [a] -> ([a],[a])
spann _ [] = ([],[])
spann f (h:t) = if f h then (h:s1, s2)
                else ([],(h:t))
    where (s1,s2) = spann f t

--f
deleteBy' :: (a -> a -> Bool) -> a -> [a] -> [a]
deleteBy' _ _ [] = []
deleteBy' f x (h:t) = if f x h then t
                      else h: deleteBy' f x t

--g
sortOn :: Ord b => (a -> b) -> [a] -> [a]
sortOn f [] = []
sortOn f (h:t) = insertOn f h (sortOn f t)
    where insertOn _ h [] = [h]
          insertOn f h (x:xs) = if f h < f x then h:x:xs
                                else x: insertOn f h xs

--2
type Polinomio = [Monomio]
type Monomio = (Float, Int)

--a
selgrau :: Int -> Polinomio -> Polinomio
selgrau x [] = []
selgrau x l = filter (\n -> x == (snd n)) l

--b
conta :: Int -> Polinomio -> Int
conta x p = length(filter(\n -> x == (snd n)) p)

--c
grau :: Polinomio -> Int
grau l = foldl (\acc n -> if acc > snd n then acc else snd n) 0 l

--d
deriv :: Polinomio -> Polinomio
deriv p = filter (/= (0,0)) $ map (\(a,b) -> if b <= 0 then (0,0) else ((a* fromIntegral b), b-1)) p

--e
calcula :: Float -> Polinomio -> Float
calcula x p = sum $ map (\(a,b) -> a* (x^b)) p
-- ou
calcula2 :: Float -> Polinomio -> Float
calcula2 x p = foldl (\acc (a,b) -> acc + a*(x^b)) 0 p 

--f
simp :: Polinomio -> Polinomio
simp p = filter (\n -> fst n /= 0) p

--g
mult :: Monomio -> Polinomio -> Polinomio
mult m p = map (\n -> (fst m * fst n, snd m + snd n)) p

--h
ordena :: Polinomio -> Polinomio
ordena p = sortOn (\n -> snd n) p

--i Assumindo que o polinómio está ordenado.
-- Se não estiver ordenado, como alternativa,
-- cria-se uma função auxiliar que recebe os mesmos parâmetros
-- mas com o Polinómio ordenado.
normaliza :: Polinomio -> Polinomio
normaliza [a] = [a]
normaliza [] = []
normaliza (h:t) = foldl (\((c,e):p) (c',e')-> if e==e'
                                         then (c+c',e):p
                                         else (c',e'):(c,e):p ) [h] t

--j
soma :: Polinomio -> Polinomio -> Polinomio
soma p1 p2 = normaliza $ (++) p1 p2

--k
produto :: Polinomio -> Polinomio -> Polinomio
produto p1 p2 = foldl (\acc x -> soma (mult x p2) acc) [] p1

--l
equiv :: Polinomio -> Polinomio -> Bool
equiv p1 p2 = if normaliza p1 == normaliza p2 then True
              else False

--3
type Mat a = [[a]]

matriz1 = [[1,2,3],
           [4,5,6],
           [7,8,9]]

matriz2 = [[1,2,3],
           [0,4,5],
           [0,0,6]]

--a
dimOK :: Mat a -> Bool
dimOK m1 = all (\x -> length x == length(head m1)) m1

--b
dimMat :: Mat a -> (Int, Int)
dimMat [] = (0,0)
dimMat m1 = (length m1, length(head m1))

--c
-- considerando que a soma de matrizes é possível
addMat :: Num a => Mat a -> Mat a -> Mat a
addMat [] _ = []
addMat _ [] = []
addMat (h:t) (x:xs) = zipWith (+) h x : addMat t xs

-- verificando se a soma de matrizes é possível
addMat2 :: Num a => Mat a -> Mat a -> Mat a
addMat2 [] _ = []
addMat2 _ [] = []
addMat2 (h:t) (x:xs) | (dimOK (h:t) && dimOK (x:xs)) && (dimMat (h:t) == dimMat(x:xs)) = zipWith (+) h x : addMat2 t xs
                     | otherwise = error "impossível"

--d
transpose :: Mat a -> Mat a
transpose ([]:_) = []
transpose (x:xs) = map (head) (x:xs) : transpose (map (tail) (x:xs))

--e
multMat :: Num a => Mat a -> Mat a -> Mat a
multMat m1 m2 = zipWith (\l1 l2 -> zipWith (+) l1 l2) m1 m2

--f
zipWMat :: (a->b->c) -> Mat a -> Mat b -> Mat c
zipWMat f m1 m2 = zipWith(\l1 l2 -> zipWith f l1 l2) m1 m2

--g
--triSup :: Num a => Mat a -> Bool
triSup (x:xs) = all (== 0) (map head xs) && triSup (map tail xs)

--h
rotateLeft :: Mat a -> Mat a 
rotateLeft [] = []
rotateLeft m = transpose (map reverse m)
