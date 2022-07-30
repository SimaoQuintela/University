--1
barra :: Eq a => [a] -> [a] -> [a]
barra l [] = l
barra [] _ = []
barra (x:xs) (h:t) = barra (delete' (x:xs) h) t 

delete' :: Eq a => [a] -> a -> [a]
delete' [] _ = [] 
delete' (x:xs) n = if x == n then xs 
                   else x : delete' xs n 
--2
type MSet a = [(a,Int)]
--a
removeMSet :: Eq a => a -> [(a,Int)] -> [(a,Int)]
removeMSet n ((a,1):t) = if n == a then t
                         else (a,1) : removeMSet n t 
removeMSet n ((a,b):t) = if n == a then (a,b-1):t
                         else (a,b) : removeMSet n t

--b
calcula :: MSet a -> ([a],Int)
calcula (h:t) = foldl (\(acc1,acc2) (c,cs) -> (c : acc1 , cs + acc2)) ([],0) (h:t)

--3
partes :: String -> Char -> [String] 
partes [] _ = []
partes (x:xs) n = takeWhile (/= n) (x:xs) : partes (delete' (dropWhile (/= n) (x:xs)) n) n

--4
--a
-- data BTree a = Empty | Node r (BTree a) (BTree a)
-- 
-- remove :: Ord a => a -> BTree a -> BTree a 
-- remove _ Empty = Empty 
-- remove n (Node r e d) | n > r = Node r e (remove n d)   
--                       | n < r = Node r (remove n e) d 
--                       | otherwise = 
-- 
--b
-- instance (Show a) => Show (BTree a) where
-- 
--     show (Empty) = "*"
--     show (Node r e d) = "(" ++ show e ++ "<-" ++ show r ++ "->" ++ show d ++ ")"
-- 
--5
sortOn' :: Ord b => (a->b) -> [a] -> [a]
sortOn' f [] = []
sortOn' f (x:xs) = insert x (sortOn' f xs)
    where insert x [] = [x]
          insert x (h:t) = if f x > f h then h : insert x t 
                           else x:h:t 
--6
--a
data FileSystem = File Nome | Dir Nome [FileSystem]
type Nome = String 

fichs :: FileSystem -> [Nome]
fichs (File n) = [n]
fichs (Dir r l) = concat (map (fichs) l) 

--b
-- dirFiles :: FileSystem -> [Nome] -> Maybe [Nome]
-- dirFiles (Dir n _) [] = Just []
-- dirFiles l [] = Just (concatMap (dirFiles) l)
-- dirFiles (Dir n l) (x:xs) = case n of 
--     x -> dirFiles l xs
--     _ -> Nothing 