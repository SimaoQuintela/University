data BTree a = Empty | Node a (BTree a) (BTree a)
             deriving Show

--a
altura :: BTree a -> Int
altura Empty = 0
altura (Node r e d) = 1 + max (altura e) (altura d)

--b
contaNodos :: BTree a -> Int
contaNodos Empty = 0
contaNodos (Node r e d) = 1 + contaNodos e + contaNodos d

--c
folhas :: BTree a -> Int 
folhas Empty = 0
folhas (Node r Empty Empty) = 1
folhas (Node r e d) = folhas e + folhas d

--d
prune :: Int -> BTree a -> BTree a
prune _ Empty = Empty
prune 0 _ = Empty
prune x (Node r e d) = Node r (prune (x-1) e) (prune (x-1) d)

--e
path :: [Bool] -> BTree a -> [a]
path _ Empty = []
path [] (Node r e d) = [r]
path (x:xs) (Node r e d) = case x of
    True -> r: path xs d
    otherwise -> r: path xs e

--f
mirror :: BTree a -> BTree a
mirror Empty = Empty
mirror (Node r e d) = Node r (mirror d) (mirror e)

--g
zipWithBT :: (a->b->c) -> BTree a -> BTree b -> BTree c
zipWithBT _ Empty _ = Empty
zipWithBT _ _ Empty = Empty
zipWithBT f (Node raiz e d) (Node s l r) = Node (f raiz s) (zipWithBT f e l) (zipWithBT f d r)

--h
unzipBT :: BTree (a,b,c) -> (BTree a, BTree b, BTree c)
unzipBT Empty = (Empty, Empty, Empty)
unzipBT (Node (ra,rb,rc) e d) = (Node ra re1 rd1, Node rb re2 rd2, Node rc re3 rd3)
    where (re1,re2,re3) = unzipBT e
          (rd1,rd2,rd3) = unzipBT d

--2
--a
minimo :: Ord a => BTree a -> a
minimo (Node r Empty Empty) = r 
minimo (Node r Empty _) = r
minimo (Node r e d) = minimo e

--b
semMinimo :: Ord a => BTree a -> BTree a
semMinimo (Node r Empty d) = d
semMinimo (Node r e d) = Node r (semMinimo e) d

--c
minSMin :: Ord a => BTree a -> (a,BTree a)
minSMin (Node r Empty d) = (r, d)
minSMin (Node r e d) = (r1, Node r r2 d)
    where (r1,r2) = minSMin e 

--d
remove :: Ord a => a -> BTree a -> BTree a
remove x (Node r e d) | x > r = Node r e (remove x d)
                      | x < r = Node r (remove x e) d 
                      | otherwise = aux x (Node r e d)
    where aux x (Node a b c) = case b of Empty -> c
                                         otherwise -> case c of Empty -> b
                                                                otherwise -> Node g b h
                                                                    where (g,h) = minSMin d
--3
type Aluno = (Numero, Nome, Regime, Classificacao)
type Numero = Int
type Nome = String
data Regime = ORD | TE | MEL deriving Show
data Classificacao = Aprov Int
                   | Rep
                   | Faltou
    deriving Show
type Turma = BTree Aluno -- árvore binária de procura (ordenada por número)


-- árvore retirada do perfil RisingFisan
turma1 :: Turma
turma1 = (Node (15,"Luís",TE,Aprov 14) (Node (12,"Joana",MEL,Faltou) (Node (7,"Diogo",TE,Rep) Empty
                                                                                               Empty) 
                                                                      (Node (14,"Lara",ORD,Aprov 19) Empty
                                                                                                     Empty))
                                        (Node (20,"Pedro",TE,Aprov 10) Empty
                                                                       (Node (25,"Sofia",ORD,Aprov 20) (Node (23,"Rita",ORD,Aprov 17) Empty
                                                                                                                                      Empty)
                                                                                                       (Node (28,"Vasco",MEL,Rep) Empty
                                                                                                                                  Empty))))

--a
inscNum :: Numero -> Turma -> Bool
inscNum _ Empty = False
inscNum n (Node (num,_,_,_) e d) | n > num = inscNum n d
                                 | n < num = inscNum n e
                                 | otherwise = True 

--b
inscNome :: Nome -> Turma -> Bool
inscNome _ Empty = False
inscNome nome (Node (_,n,_,_) e d) = if nome == n then True
                                    else inscNome nome e || inscNome nome d 

--c
trabEst :: Turma -> [(Numero, Nome)]
trabEst Empty = []
trabEst (Node (num,nome,reg,_) e d) = case reg of 
    TE -> trabEst e ++ [(num,nome)] ++ trabEst d
    otherwise -> trabEst e ++ trabEst d

--d
nota :: Numero -> Turma -> Maybe Classificacao
nota n Empty = Nothing
nota n (Node (num,_,_,classi) e d) | n > num = nota n d
                                   | n < num = nota n e
                                   | otherwise = Just classi

--e ver isto, problemas com os tipos
percFaltas :: Turma -> Float
percFaltas Empty = 0
percFaltas turma = a*100 / b
    where a = fromIntegral (faltas turma) :: Float
          b = fromIntegral (numAlunos turma) :: Float

faltas :: Turma -> Int
faltas Empty = 0
faltas (Node (_,_,_,classi) e d) = case classi of
    Faltou -> 1 + faltas e + faltas d
    otherwise -> faltas e + faltas d

numAlunos :: Turma -> Int
numAlunos Empty = 0
numAlunos (Node r e d) =  1 + numAlunos e + numAlunos d

--f 
mediaAprov :: Turma -> Float
mediaAprov turma = 100*a / b 
    where a = fromIntegral (notasAprov turma) :: Float 
          b = fromIntegral (numeroDeAprov turma) :: Float

notasAprov ::  Turma -> Int
notasAprov (Node (_,_,_,classi) e d) = case classi of
    Aprov x -> x + notasAprov e + notasAprov d
    otherwise -> notasAprov e + notasAprov d

numeroDeAprov :: Turma -> Int
numeroDeAprov (Node (_,_,_,classi) e d) = case classi of
    Aprov _ -> 1 + numeroDeAprov e + numeroDeAprov d
    otherwise -> numeroDeAprov e + numeroDeAprov d