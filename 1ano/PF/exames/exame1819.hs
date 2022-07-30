--1
--a
isSorted :: (Ord a) => [a] -> Bool
isSorted [] = True
isSorted (x:y:xs) = if x <= y then isSorted (y:xs)
                    else False

--b
inits :: [a] -> [[a]]
inits [] = [[]]
inits l = inits (init l) ++ [l]

--2
maximumMB :: (Ord a) => [Maybe a] -> Maybe a
maximumMB [Just a] = Just a
maximumMB (x:y:xs) = case x of
    Just c -> case y of
        Just d -> if c >= d then maximumMB (x:xs)
                  else maximumMB (y:xs)
        Nothing -> maximumMB (x:xs)
    Nothing -> maximumMB (y:xs)

--3
data LTree a = Tip a | Fork (LTree a) (LTree a)
--a 
listaLT :: LTree a -> [a]
listaLT (Tip a) = [a]
listaLT (Fork l r) = listaLT l ++ listaLT r

--b
instance (Show a) => Show (LTree a) where 
    show (Tip a) = show a ++ "\n"
    show (Fork l r) = prof 1 l ++ prof 1 r 
    
prof :: (Show a) => Int -> LTree a -> String
prof n (Tip a) = replicate n '.' ++ show a ++ "\n"
prof n (Fork l r) = prof (n+1) l ++ prof (n+1) r 

--4
maxSumInit :: (Num a,Ord a) => [a] -> a
maxSumInit l = foldl (\acc x -> max (sum x) acc) (sum l) (inits l)

--5
type RelP a = [(a,a)] 
type RelL a = [(a,[a])]
type RelF a = ([a], a -> [a])
--a repetir 
convPL :: (Eq a) => RelP a -> RelL a
convPL [(x,y)] = [(x,[y])]
convPL (h:t) = junta h (convPL t)
    where junta (a,b) l = if a `elem` map (fst) l 
                          then map (\(c,d) -> if c == a then (c,b:d) else (c,d)) l 
                          else (a,[b]):l

