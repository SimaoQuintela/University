--1
--a
unlines' :: [String] -> String
unlines' [] = []
unlines' (x:xs) = x ++ "\n" ++ unlines' xs 

--b  tenho de otimizar esta shit  
barra :: (Ord a) => [a] -> [a] -> [a]
barra (h:t) (x:xs) = barra2 (h:t) (ordena (x:xs)) 

ordena :: Ord a => [a] -> [a]
ordena [] = []
ordena (x:xs) = insert x (ordena xs)
    where insert x [] = [x]
          insert x (h:t) = if x < h then x: (h:t) 
                           else h: insert x t 

barra2 :: Eq a => [a] -> [a] -> [a]
barra2 l [] = l 
barra2 [] _ = []
barra2 (x:xs) (h:t) = if x == h then barra2 xs t 
                      else x : barra2 xs t

--2
data Seq a = Nil | Inicio a (Seq a) | Fim (Seq a) a 
--a
primeiro :: Seq a -> a 
primeiro (Inicio a s) = a 
primeiro (Fim Nil a) = a 
primeiro (Fim s a) = primeiro s

--b
semUltimo :: Seq a -> Seq a 
semUltimo (Inicio a Nil) = Nil 
semUltimo (Inicio a s) = Inicio a (semUltimo s)
semUltimo (Fim s a) = s

--3
data BTree a = Empty | Node a (BTree a) (BTree a)
--a
prune :: Int -> BTree a -> BTree a
prune _ Empty = Empty 
prune 1 (Node r e d) = Node r Empty Empty 
prune x (Node r e d) = Node r (prune (x-1) e) (prune (x-1) d) 

--b
semMinimo :: Ord a => BTree a -> BTree a
semMinimo Empty = Empty 
semMinimo (Node r Empty d) = d
semMinimo (Node r e d) = Node r (semMinimo e) d 

--4
--a
exemplo = ["..R.",
           "R...",
           "...R",
           ".R.."]

type Tabuleiro = [String]
 
--posicoes :: Tabuleiro -> [(Int,Int)]
--posicoes [] = []
--posicoes (x:xs) = (colunas x ,  ) : posicoes xs 
--
--colunas :: String -> Int 
--colunas (x:xs) = case x of
--    '.' -> 1 + colunas xs
--    'R' -> 0
--
--linhas :: Tabuleiro -> Int 



posicoes :: Tabuleiro -> [(Int,Int)]
posicoes [] = []
posicoes (x:xs) = aux x 0 (length x - length (x:xs)) ++ posicoes xs 

aux :: String -> Int -> Int -> [(Int,Int)]
aux [] _ _ = []
aux (x:xs) acc1 acc2 = case x of 
  '.' -> aux xs (acc1+1) (acc2)
  'R' -> [(acc1,acc2)] ++ aux xs (acc1+1) acc2 