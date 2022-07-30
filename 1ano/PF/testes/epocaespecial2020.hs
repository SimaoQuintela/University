-- exame época especial 
--1
--a
subst :: Eq a => (a,a) -> [a] -> [a]
subst _ [] = [] 
subst (a,b) (x:xs) = if x == a then b : subst (a,b) xs 
                     else x : subst (a,b) xs

--b
posicoes' :: [a] -> [Int] -> [a]
posicoes' l [] = [] 
posicoes' l (x:xs) = pega l x ++ posicoes' l xs 
    where pega [] n = []
          pega (h:t) 1 = [h] 
          pega (h:t) n = pega t (n-1)
          
--2
data Tree a b = Folha b | Nodo a (Tree a b) (Tree a b)

--a
folh :: Tree a b -> [b]
folh (Folha a) = [a]
folh (Nodo r e d) = folh e ++ folh d 

--b
somas :: Tree Float Int -> (Float , Int)
somas (Folha b) = (0 , b)
somas (Nodo r e d) = (r + x + x' , y + y')
    where (x,y) = somas e 
          (x',y') = somas d 

--3
rotateLeft' :: Mat a -> Mat a 
rotateLeft' (x:xs) = reverse (map head (x:xs) : rotateLeft' (map tail (x:xs)))

--4
type Filme = (Titulo, Realizador, [Actor], Genero , Ano)
type Titulo = String 
type Realizador = String 
type Actor = String 
type Ano = Int 

data Genero = Comedia | Drama | Ficcao | Accao | Animacao | Documentario
            deriving Eq 

type Filmes = [Filme]

--a
doRealizador :: Filmes -> Realizador -> [Titulo]
doRealizador [] _ = []
doRealizador ((a,b,c,d,e):xs) r = if r == b then a : doRealizador xs r 
                                  else doRealizador xs r 

--b
doActor :: Filmes -> Actor -> [Titulo]
doActor [] _ = [] 
doActor ((a,b,c,d,e):xs) x = if elem x c then a : doActor xs x 
                             else doActor xs x

--c
-- aux :: Filme -> (Ano, Titulo)
-- aux ((a,_,_,_,e):xs) = (e,a)

-- --5
data Avaliacao = NaoVi 
               | Pontos Int  -- pontuação entre 1 e 5

type FilmesAval = [(Filme,[Avaliacao])]

--a não está totalmente correto
-- avalia :: FilmesAval -> IO FilmesAval 
-- avalia ((a,b):xs) = do  putStrLn "Insira o nome do filme"
--                         x <- getLine 
--                         if elem x (listaDeFilmes ((a,b):xs)) then putStrLn "Insira a classificação do filme"
--                         else putStrLn "Não existe esse filme" ; 
--                         y <- getLine 
--                         return (adicionaClass ((a,b):xs) (x,[y]))
-- 
-- 
-- adicionaClass :: FilmesAval -> (Filme,[Avaliacao]) -> FilmesAval
-- adicionaClass ((a,b):xs) (c,d) = if a == c then ((a,b++d):xs)
--                                  else (a,b) : adicionaClass xs (c,d)
-- 
-- listaDeFilmes :: FilmesAval -> [Filme]
-- listaDeFilmes [] = [] 
-- listaDeFilmes ((a,b):xs) = a : listaDeFilmes xs 

