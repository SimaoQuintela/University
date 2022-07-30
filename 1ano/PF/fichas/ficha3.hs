{-
import Ficha1

type Etapa = (Hora2,Hora2)
type Viagem = [Etapa]

--a
bemConstruido :: Etapa -> Bool
bemConstruido (h1,h2) = ((valida2 h1) && (valida2 h2)) && (depois h2 h1)

--b
viagemBemConstruida :: Viagem -> Bool
viagemBemConstruida [] = True
viagemBemConstruida [h] = bemConstruido h
viagemBemConstruida ((h1,h2):(h3,h4):t) = bemConstruido (h1,h2) && bemConstruido (h2,h3) && viagemBemConstruida ((h3,h4):t)

--c
partidaEchegada :: Viagem -> (Hora2,Hora2)
partidaEchegada [(x,y)] = (x,y)
partidaEchegada (h1:t) = (fst h1,snd (last t))

--d
tempoDeViagem :: Viagem -> Hora2
tempoDeViagem [(h1,h2)] = diferencaHora h1 h2
tempoDeViagem ((h1,h2):t) = adiciona (horaParaMin (diferencaHora h1 h2)) (tempoDeViagem t) 

--e
tempoDeEspera :: Viagem -> Hora2
tempoDeEspera l =  diferencaHora (tempoTotalDeViagem l)  (tempoDeViagem l) 

--Ou
tempoDeEspera2 :: Viagem -> Hora2
tempoDeEspera2 ((e1,e2):(e3,e4):t) = adiciona (diferencaHora e2 e3) (horaParaMin (tempoDeEspera2 (e3,e4):t))

--f
tempoTotalDeViagem :: Viagem -> Hora2
tempoTotalDeViagem ((h1,h2):t) = diferencaHora h1 (snd (last t))


--2
type Poligonal = [Ponto]
--a
compLinha :: Poligonal -> Double
compLinha [x] = 0
compLinha (x:y:ys) = dist x y + compLinha (y:ys)

--b
fechada :: Poligonal -> Bool
fechada [p1,p2] = False
fechada [p1,p2,p3] = p1 == p3
fechada (p1:p2:p3:ps) = fechada (p1:p3:ps)

--c
triangula :: Poligonal -> [Figura]
triangula [p1,p2,p3] = [(Triangulo p1 p2 p3)]
triangula (p1:p2:p3:ps) = (Triangulo p1 p2 p3):triangula (p1:p3:ps)

--e
mover :: Poligonal -> Ponto -> Poligonal 
mover [] p = [p]
mover l p = p:l 
-}
--3
data Contacto = Casa Integer
              | Trab Integer
              | Tlm Integer
              | Email String
              deriving Show

type Nome = String
type Agenda = [(Nome, [Contacto])]

--a
acrescEmail :: Nome -> String -> Agenda -> Agenda
acrescEmail x y [] = [(x, [Email y])] 
acrescEmail x y agenda = [(x,[Email y])] ++ agenda

--b
verEmails :: Nome -> Agenda -> Maybe [String]
verEmails n [] = Nothing
verEmails n ((a,(x:xs)):t) = if n == a then Just (emails (x:xs))
                             else verEmails n t

emails :: [Contacto] -> [String]
emails [] = []
emails (x:xs) = case x of
    Email y -> y : emails xs
    otherwise -> emails xs

--c
consTelefs :: [Contacto] -> [Integer]
consTelefs [] = []
consTelefs (x:xs) = case x of 
    Casa y -> y : consTelefs xs
    Trab y -> y : consTelefs xs
    Tlm y ->  y : consTelefs xs
    otherwise -> consTelefs xs

--d
casa :: Nome -> Agenda -> Maybe Integer
casa n [] = Nothing
casa n ((nome, (x:xs)):t) = if n == nome then case x of
                                                  Casa x -> Just x
                                                  _ -> casa n [(nome, xs)]
                            else casa n t 

--4
{-
type Dia = Int
type Mes = Int
type Ano = Int
--type Nome = String

data Data = D Dia Mes Ano
          deriving Show

type TabDN = [(Nome,Data)]

--a
procura :: Nome -> TabDN -> Maybe Data
procura [] _ = Nothing
procura _ [] = Nothing
procura nome1 ((nome2,dataa):xs) | nome1 == nome2 = Just dataa
                                 | otherwise = procura nome1 xs

--b
idade :: Data -> Nome -> TabDN -> Maybe Int
idade _ _ [] = Nothing
idade (D d m a) nome ((n,(D d1 m1 a1)):xs) | nome == n && ((m > m1) || (m == m1 && d > d1) || (m == m1 && d == d1)) = Just (a-a1)
                                           | nome == n && ((m > m1) || (m==m1 && d < d1)) = Just (a-a1-1)
                                           | otherwise = idade (D d m a) nome xs

--c
anterior :: Data -> Data -> Bool
anterior (D d m a) (D d1 m1 a1) | a > a1 = False
                                | a == a1 && m > m1 = False
                                | a == a1 && m == m1 && d > d1 = False
                                | d == d1 && m == m1 && a == a1 = False
                                |otherwise = True


--d
ordena :: TabDN -> TabDN
ordena [] = []
ordena (x:xs) = insere x (ordena xs)
    where insere x [] = [x]
          insere (a,b) ((c,d):t) = if anterior b d then (a,b):(c,d):t
                                      else (c,d): insere (a,b) t

--e
porIdade :: Data -> TabDN -> [(Nome,Int)]
porIdade _ [] = []
porIdade (D d m a) l = (n,idade) : porIdade (D d m a) ts 
    where ((n,D dx mx ax):ts) = ordena l
          idade = if m > mx || mx == m && d > dx then (a-ax)
                  else ((a-ax)-1)
-}
-----------
--5
data Movimento = Credito Float | Debito Float
               deriving Show

data Data = D Int Int Int
          deriving Show

data Extracto = Ext Float [(Data,String,Movimento)]
              deriving Show

--a
extValor :: Extracto -> Float -> [Movimento]
extValor (Ext _ []) _ = []
extValor (Ext x1 ((a,b,c):t)) x2 | x1 > x2 = c : extValor (Ext x1 t) x2
                                 | otherwise = extValor (Ext x1 t) x2

--b
filtro :: Extracto -> [String] -> [(Data,Movimento)]
filtro (Ext x ((a,b,c):xs)) l = if elem b l then (a,c):filtro (Ext x xs) l
                                    else filtro (Ext x xs) l

--c
creDeb :: Extracto -> (Float,Float)
creDeb (Ext x ((a,b,c):xs)) = case c of
    Credito c -> (c+ cre, deb)
        where (cre,deb) = creDeb (Ext x xs)
    Debito c -> (cre, c+deb)
        where (cre,deb) = creDeb (Ext x xs)

--d
