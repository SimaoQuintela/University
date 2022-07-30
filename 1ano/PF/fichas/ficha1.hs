--1. a)
perimetro :: Double -> Double
perimetro x = 2*pi*x 

--b)
dist :: (Double, Double) -> (Double, Double) -> Double
dist (x1,y1) (x2,y2) = sqrt(x-y)
    where x = (x2-x1)^2
          y = (y2-y1)^2

--c)
primUlt :: [a] -> (a,a)
primUlt (h:t) = (h, last(h:t))

--d)
multiplo :: Int -> Int -> Bool
multiplo m n = if mod m n == 0 then True
               else False

--e)
truncaImpar :: [a] -> [a]
truncaImpar [] = []
truncaImpar (h:t) = if mod (length(h:t)) 2 /= 0 then t
                    else (h:t)

--f)
max2 :: Int -> Int -> Int
max2 x y =  if x >= y then x
            else y

--g)
max3 :: Int -> Int -> Int -> Int
max3 x y z = max2 (max2 x y) z

--2 a.
nRaizes :: Float -> Float -> Float -> Int
nRaizes x2 x1 x0 | raizes == 0 = 1
                 | raizes > 0 = 2
                 | otherwise = 0
    where raizes = sqrt(x1^2 -4*x2*x0)

--b
raizes :: Float -> Float -> Float -> [Float]
raizes x2 x1 x0  | nRaizes x2 x1 x0 == 0 = []
                 | nRaizes x2 x1 x0 == 1 = [-x1/2*x2]
                 | otherwise = [(-x1 + raizes) / 2*x2, (-x1 - raizes) / 2*x2]
    where raizes = sqrt(x1^2 -4*x2*x0)

--3
type Hora = (Int, Int)

--a
valida :: Hora -> Bool
valida (hora, minuto) = if (hora > 0 && hora < 24) && (minuto >= 0 && minuto < 60) then True
                        else False

--b
comparacao :: Hora -> Hora -> Bool
comparacao (h1,m1) (h2,m2) | h1 > h2 = True
                           | h1 == h2 && m1 > m2 = True
                           | otherwise = False

--c
converter :: Hora -> Int
converter (h,m) = h * 60 + m


--d
converter2 :: Int -> Hora
converter2 x = (div x 60, mod x 60) 

--e
diferenca :: Hora -> Hora -> Int
diferenca h1 h2 = abs(converter h1 - converter h2)

--f
adicionar :: Int -> Hora -> Hora
adicionar x hora = converter2(x + converter hora)

--5
data Semaforo = Verde | Amarelo | Vermelho deriving(Show, Eq)

--a
next :: Semaforo -> Semaforo
next x = case x of
  Verde -> Amarelo
  Amarelo -> Vermelho
  otherwise -> Verde

--b
stop :: Semaforo -> Bool
stop x = if x == Vermelho then True
         else False 

--6
data Ponto = Cartesiano Double Double | Polar Double Double
             deriving(Show, Eq)

--7
data Figura = Circulo Ponto Double
            | Rectangulo Ponto Ponto
            | Triangulo Ponto Ponto Ponto
              deriving(Show, Eq)
--a
poligono :: Figura -> Bool
poligono x = case x of 
  Circulo _ _ -> False
  _ -> True

--8
