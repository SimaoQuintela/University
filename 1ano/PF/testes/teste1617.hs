type MSet a = [(a,Int)]
--1
--a
cardMSet :: MSet a -> Int 
cardMSet [] = 0 
cardMSet ((x,y):t) = y + cardMSet t 

--b
moda :: MSet a -> [a]
moda [(x,y)] = replicate y x
moda ((x,y):(z,w):t) = if y > w then moda ((x,y):t)
                       else moda ((z,w):t)

--c
converteMSet :: MSet a -> [a]
converteMSet [] = []
converteMSet ((x,y):t) = replicate y x ++ converteMSet t 

--d 
addNcopies :: Eq a => MSet a -> a -> Int -> MSet a 
addNcopies [] x y = [(x,y)]
addNcopies ((x,y):t) a b | elem a (list ((x,y):t)) = if a == x then ((x,y+b):t) else [(x,y)] ++ addNcopies t a b
                         | otherwise =  if b > y then (a,b) : ((x,y) : t)
                                        else [(x,y)] ++ addNcopies t a b

list :: MSet a -> [a]
list [] = []
list ((x,y):t) = x : list t

--2
ex2 :: SReais
ex2 = Uniao (Uniao (AA 4.2 5.5) (AF 3.1 7.0)) (FF (-12.3) 30.0)
--a
data SReais = AA Double Double | FF Double Double 
            | AF Double Double | FA Double Double 
            | Uniao SReais SReais

instance Show SReais where 
    show (Uniao a b) = "(" ++ show a ++ " U " ++ show b ++ ")"
    show intervalo = ch1 ++ num1 ++ " , " ++ num2 ++ ch2
        where (ch1,num1,num2,ch2) = case intervalo of AA a b -> ("]",show a, show b, "[")
                                                      AF a b -> ("]",show a,show b,"]")
                                                      FA a b -> ("[",show a,show b,"[")
                                                      FF a b -> ("[",show a,show b,"]")

--b
pertence :: Double -> SReais -> Bool
pertence n (AA x y) = if n > x && n < y then True 
                      else False
pertence n (FF x y) = if n >= x && n <= y then True 
                      else False 
pertence n (AF x y) = if n > x && n < y then True 
                      else False 
pertence n (FA x y) = if n >= x && n < y then True 
                      else False 
pertence n (Uniao s1 s2) = pertence n s1 || pertence n s2 







