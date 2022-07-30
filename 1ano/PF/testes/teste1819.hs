import Data.Char
--a
elemIndices :: Eq a => a -> [a] -> [Int]
elemIndices x [] = []
elemIndices x l = aux x l 0

aux :: Eq a => a -> [a] -> Int -> [Int]
aux _ [] _ = []
aux x (h:t) n = if x == h then [n] ++ aux x t (n+1)
                else aux x t (n+1)
--b
isso :: Eq a => [a] ->[a] -> Bool 
isso [] l = True 
isso l [] = False 
isso (x:xs) (h:t) | x == h = isso xs t 
                  | otherwise = isso (x:xs) t 

--2
data BTree a = Empty | Node a (BTree a) (BTree a)
--a
lookupAP :: Ord a => a -> BTree (a,b) -> Maybe b 
lookupAP x Empty = Nothing 
lookupAP x (Node (a,b) l r) | x == a = Just b
                            | x < a = lookupAP x l 
                            | otherwise = lookupAP x r 
--b
zipWithBT :: (a->b->c) -> BTree a -> BTree b -> BTree c 
zipWithBT _ Empty _ = Empty
zipWithBT _ _ Empty = Empty
zipWithBT f (Node r e d) (Node rr ee dd) = Node (f r rr) (zipWithBT f e ee) (zipWithBT f d dd)

--3
digitAlpha :: String -> (String,String)
digitAlpha [] = ([],[])
digitAlpha (x:xs) = if isDigit x then (x:a,b)
                    else (a,x:b) 
    where (a,b) = digitAlpha xs

--4
data Seq a = Nil | Cons a (Seq a) | App (Seq a) (Seq a)
--a
firstSeq :: Seq a -> a 
firstSeq (Cons a s) = a 
firstSeq (App Nil s) = firstSeq s 
firstSeq (App s _) = firstSeq s 

--b    repetir
dropSeq :: Int -> Seq a -> Seq a 
dropSeq _ Nil = Nil
dropSeq n (Cons x s) = dropSeq (n-1) s 
dropSeq n (App s1 s2) | n > x = dropSeq (n-x) s2
                      | n == x = s2
                      | otherwise = App (dropSeq n s1) s2
    where x = contaCons s1

contaCons :: Seq a -> Int 
contaCons Nil = 0
contaCons (Cons a s) = 1+ contaCons s 
contaCons (App s1 s2) = contaCons s1 + contaCons s2

--c repetir
instance Show a => Show (Seq a) where
    show x = "<<" ++ sh0w x ++ ">>"

sh0w :: Show a => Seq a -> String
sh0w Nil = ""
sh0w (Cons a Nil) = show a 
sh0w (Cons a s) = show a ++ sh0w s 
sh0w (App s1 s2) = sh0w s1 ++ sh0w s2 
