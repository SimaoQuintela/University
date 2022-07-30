data ExpInt = Const Int
            | Simetrico ExpInt
            | Mais ExpInt ExpInt
            | Menos ExpInt ExpInt
            | Mult ExpInt ExpInt

--1
--a
calcula :: ExpInt -> Int
calcula (Const n) = n
calcula x = case x of
    Simetrico k -> -1 * calcula k
    Mais k1 k2 -> calcula k1 + calcula k2
    Menos k1 k2 -> calcula k1 - calcula k2
    Mult k1 k2 -> calcula k1 * calcula k2

--b
infixa :: ExpInt -> String
infixa x = case x of
    Const n -> show n
    Simetrico k -> "-(" ++ infixa k
    Mais k1 k2 -> "(" ++ infixa k1 ++ " + " ++ infixa k2 ++ ")"
    Menos k1 k2 -> "("  ++ infixa k1 ++ " - " ++ infixa k2 ++ ")"
    Mult k1 k2 -> "(" ++ infixa k1 ++ " * " ++ infixa k2 ++ ")"

--c
posfixa :: ExpInt -> String
posfixa (Const n) = show n
posfixa x = case x of 
    Simetrico n -> show n ++ "-"
    Mais k1 k2 -> show k1 ++ " " ++ show k2 ++ "+"
    Menos k1 k2 -> show k1 ++ " " ++ show k2 ++ "-"
    Mult k1 k2 -> show k1 ++ " " ++ show k2 ++ "*"

--2
data RTree a = R a [RTree a]

--a
soma :: Num a => RTree a -> a
soma (R a []) = a
soma (R a l) = a + sum (map soma l)

--b
altura :: RTree a -> Int
altura (R a []) = 1
altura (R a l) = 1 + maximum(map altura l)

--c
prune :: Int -> RTree a -> RTree a
prune 0 R a l = R a []
prune x (R a l) = R a (map (prune (x-1)) l)

--d
mirror :: RTree a -> RTree a
mirror (R a l) = R a (map mirror (reverse l))

--e
postOrder :: RTree a -> [a]
postOrder (R a l) = concat (map postOrder l) ++ [a]

--3
data LTree a = Tip a | Fork (LTree a) (LTree a)

--a
ltSum :: Num a => LTree a -> a
ltSum (Tip a) = a
ltSum (Fork e d) = ltSum e + ltSum d

--b
listaLT :: LTree a -> [a]
listaLT (Tip a) = [a]
listaLT (Fork e d) = listaLT e ++ listaLT d

--c
ltHeight :: LTree a -> Int
ltHeight (Tip a) = 0
ltHeight (Fork e d) = 1+ max (ltHeight e) (ltHeight d)

--4
data FTree a b = Leaf b | No a (FTree a b) (FTree a b)

--a
splitFTree :: FTree a b -> (BTree a, LTree b)
splitFTree (Leaf b) = (Node b Empty Empty, Tip a)
splitFTree (No a e d) = (Node a e2 d2, Fork e2 d2)
    where e2 = splitFTree e
          d2 = splitFTree d

--b
joinTrees :: BTree a -> LTree b -> Maybe (FTree a b)
joinTrees _ (Tip a) = Just (Leaf a)
joinTrees (Node r e d) (Fork e2 d2) = Just (No r e3 d3)
    where e3 = joinTrees e e2
          d3 = joinTrees d d2
joinTrees _ _ = Nothing