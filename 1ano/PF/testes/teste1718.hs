--1
insert :: Ord a => a -> [a] -> [a]
insert x [] = [x]
insert x (h:t) = if x > h then h: insert x t 
                 else x : (h:t)

--2
catMaybes :: [Maybe a] -> [a]
catMaybes [] = []
catMaybes (x:xs) = case x of 
    Just a -> a : catMaybes xs 
    Nothing -> catMaybes xs 

--3
data Exp a = Const a 
           | Var String 
           | Mais (Exp a) (Exp a)
           | Mult (Exp a) (Exp a)

instance Show a => Show (Exp a) where 
    show (Const a) = show a
    show (Var a) = a 
    show (Mais x y) = "(" ++ show x ++ "+" ++ show y ++ ")"
    show (Mult x y) = "(" ++ show x ++ "*" ++ show y ++ ")"

--4
sortOn :: Ord b => (a->b) -> [a] -> [a]
sortOn _ [] = []
sortOn f (h:t) = insert' h (sortOn f t)
    where insert' x [] = [x]
          insert' x (h:t) = if f x > f h then h : insert' x t 
                            else x : (h:t) 

--5
--a faz 2 passagens 
-- amplitude :: [Int] -> Int 
-- amplitude [] = 0 
-- amplitude l = maximum l - minimum l 

-- faz 1 passagem 
amplitude ::  [Int] -> Int
amplitude [] = 0
amplitude l = mx - mn
    where (mx,mn) = foldl (\(a,b) n -> (if n > a then n else a,if n < b then n else b)) (head l,head l) l 

--6
data Imagem = Quadrado Int 
            | Mover (Int,Int) Imagem 
            | Juntar [Imagem]

--a
conta :: Imagem -> Int 
conta (Quadrado _) = 1 
conta (Mover (_,_) i) = conta i 
conta (Juntar i) = sum (map conta i)
