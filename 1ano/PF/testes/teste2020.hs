--a
intersect :: Eq a => [a] -> [a] -> [a]
intersect l [] = []
intersect [] l = []
intersect (x:xs) l = if elem x l then x : intersect xs l 
                     else intersect xs l 

--b
tails :: [a] -> [[a]]
tails [] = [[]] 
tails (x:xs) = (x:xs) : tails xs

--2
type ConjInt = [Intervalo]
type Intervalo = (Int,Int)

--a
elems :: ConjInt -> [Int]
elems [] = []
elems ((h,t):xs) = if h == t then t : elems xs 
                   else h : elems ((h+1,t):xs)

--b
geraconj :: [Int] -> ConjInt
geraconj [] = []
geraconj (x:xs) = (x,d) : geraconj (dropWhile (<= d) xs)
    where d = foldl (\acc x -> if x == succ acc then x else acc) x xs 

--3
data Contacto = Casa Integer 
              | Trab Integer
              | Tlm Integer 
              | Email String 
    deriving (Show)
type Nome = String 
type Agenda = [(Nome, [Contacto])]
--a
acrescEmail :: Nome -> String -> Agenda -> Agenda 
acrescEmail n e [] = [(n,[Email e])]
acrescEmail n e l = l ++ [(n,[Email e])]

--b repetir isto 
verEmails :: Nome -> Agenda -> Maybe [String]
verEmails nome [(n,c)]= if nome == n then Just (map (\x -> case x of Email e -> e) c) else Nothing 
verEmails nome ((n,c):agenda) = if nome == n then verEmails nome [(n,c)] else verEmails nome agenda

--c
consulta :: [Contacto] -> ([Integer],[String])
consulta [] = ([],[])
consulta (x:xs) = case x of 
    Casa x -> (x:a,b)
    Trab x -> (x:a,b)
    Tlm x -> (x:a,b)
    Email x -> (a, x:b)
  where (a,b) = consulta xs


agenda1 = [("Sofia", [Casa 123456789, Tlm 987654321, Email "abc@def.ghi", Email "f@mendess.xyz"]),("Luís", [Tlm 69420]),("Rita", [Trab 58008])]
--d
consultaIO :: Agenda -> IO ()
consultaIO ((n,c):xs) = do x <- getLine
                           let contactos = aux x ((n,c):xs)
                           putStr (concat [show x ++ "\n" | x <- contactos]) 

                           where aux _ [] = []
                                 aux x ((n,c):xs) = if x == n then c
                                                    else aux x xs

--4
data RTree a = R a [RTree a] deriving (Show,Eq)
--a repetir 
paths :: RTree a -> [[a]]
paths (R a []) = [[a]] 
paths (R node branches) = [ node : x | x <- concat [paths branch | branch <- branches]]

--b ????????