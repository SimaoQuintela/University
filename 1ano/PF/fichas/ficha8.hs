--1
data Frac = F Integer Integer

--a
mdc :: Integer -> Integer -> Integer
mdc x _ = x
mdc _ x = x
mdc x y = mdc y (mod x y)

normaliza :: Frac -> Frac
normaliza (F x y) = F (div x m) (div y m)
    where m = mdc x y

--b
instance Eq Frac where
	(F x y) == (F x1 y1) = (x*y1) == (y*x1)

--c
instance Ord Frac where
	compare (F x y) (F x1 y1)
      |c1 < c2 = LT
      |c1 == c2 = EQ
      |c1 > c2 = GT
      where
      	c1 = (fromIntegral x) / (fromIntegral y)
      	c2 = (fromIntegral x1) / (fromIntegral y1)

--d
instance Show Frac where
    (F x y) = show x ++ "/" ++ show y

--e
instance Num Frac where
--	(+), (*), (-) :: a -> a -> a
--  negate, abs, signum :: a -> a
--  fromInteger :: Integer -> a
    (F x y) + (F x1 y1) = normaliza (F (x*y1 + y*x1) (y*y1))
    (F x y) * (F x1 y1) = normaliza (F (x*y) (x1*y1))
    (F x y) - (F x1 y1) = normaliza (F (x*y1 - y*x1) (y*y1))
    negate (F x y) = F (-1*x) y
    abs (F x y) = F (abs x) (abs y)
    signum (F x y) | (x > 0 && y > 0) || (x<0 && y<0) = 1
                   | x == 0 = 0
                   | otherwise = -1
    fromInteger x = F x 1

--2
data Exp a = Const a
           | Simetrico (Exp a)
           | Mais (Exp a) (Exp a)
           | Menos (Exp a) (Exp a)
           | Mult (Exp a) (Exp a)

--a
instance Show a => Show (Exp a) where
    show (Const a) = show a
    show (Simetrico a) = "(- " ++ show a ++ ")"
    show (Mais a b) = "(" ++ show a ++ " + " ++ show b ++ ")"
    show (Menos a b) = "(" ++ show a ++ " - " ++ show b ++ ")"
    show (Mult a b) = "(" ++ show a ++ " * " ++ show b ++ ")"
--b
valor :: (Num a) => Exp a -> a
valor (Const a) = a
valor (Simetrico a) = - (valor a)
valor (Mais a b) = valor a + valor b
valor (Menos a b) = valor a - valor b
valor (Mult a b) = valor a * valor b

instance Eq a => Eq (Exp a) where 
    x == y = valor x == valor y

--c
instance Num a => Num (Frac a) where
    x + y = Const (valorDe x + valorDe y)
    x - y = Const (valorDe x - valorDe y)
    x * y = Const (valorDe x * valorDe y)
    negate (Const a) = Const (- a)
    negate (Simetrico a) = a
    negate (Mais a b) = Mais (- a) (- b)
    negate (Menos a b) = Menos b a
    negate (Mult a b) = Mult (-a) b
    fromInteger x = Const (fromInteger x)
    abs (Const a) = Const (abs a)
    abs (Simetrico a) = abs a
    abs (Mais a b) = abs (a + b)
    abs (Menos a b) = abs (a - b)
    abs (Mult a b) = abs (a * b)
    signum (Const a) = Const (if abs a == a then if a == 0 then 0 else 1 else (-1))
    signum (Simetrico a) = - signum a
    signum (Mais a b) = Const (if abs (a + b) == a + b then if a + b == 0 then 0 else 1 else (-1))
    signum (Menos a b) = Const (if abs (a - b) == a - b then if a - b == 0 then 0 else 1 else (-1))
    signum (Mult a b) = Const (if abs (a * b) == a * b then if a * b == 0 then 0 else 1 else (-1))


--3
data Movimento = Credito Float | Debito Float
data Data = D Int Int Int
data Extracto = Ext Float [(Data, String, Movimento)]

--a
instance Ord Data where
    compare (D dia1 mes1 ano1) (D dia2 mes2 ano2) | ano1 > ano2 || ano1 == ano2 && (mes1 > mes2 || mes1 == mes2 && dia1 > dia2) = GT
                                                  | ano1 == ano2 && mes1 == mes2 && dia1 == dia2 = EQ
                                                  | otherwise = LT

--b
instance Show Data where
	show (D d m a) = show d ++ "/" ++ show m ++ "/" ++ show a

--c
ordena :: Extracto -> Extracto 
ordena (Ext n l) = (Ext n (sortBy (\(data1,_,_) (data2,_,_) -> compare data1 data2) l ))

--d
instance Show Extracto where 
    show (Ext n l) = "Saldo anterior:" ++ show n ++
                     "\n-------------------------------------------------" ++
                     "\nData           Descricao        Credito    Debito" ++
                     "\n-------------------------------------------------\n" ++ concatMap (\(dat,str,mov) -> show dat ++ replicate (11- (length (show dat ))) ' ' ++ map (toUpper) str ++ "    \n") l ++
                     "--------------------------------------------------" ++
                     "\nSaldo actual:" ++ show (saldo (Ext n l))

saldo :: Extracto -> Float
saldo (Ext a l) = foldl (\acc (_,_,mov) -> case mov of Credito n -> (acc +n)
                                                       Debito n -> (acc -n)) a l