--1
elemento :: [a] -> Int -> a 
elemento (x:xs) n = if n == 0 then x 
                    else elemento xs (n-1)

--2
data Movimento = Norte | Sul | Este | Oeste deriving Show 

posicao :: (Int,Int) -> [Movimento] -> (Int,Int)
posicao (x,y) [] = (x,y)
posicao (x,y) (h:t) = case h of 
    Norte -> posicao (x,y+1) t
    Sul -> posicao (x,y-1) t 
    Este -> posicao (x+1,y) t 
    otherwise -> posicao (x-1,y) t 

any' :: (a -> Bool) -> [a] -> Bool
any' f [] = False  
any' f (x:xs) = if f x == True then True 
               else any' f xs

--4 refazer depois
type Mat a = [[a]]

triSup :: (Num a,Eq a) => Mat a -> Bool
triSup [] =  True 
triSup ((x:xs):t) = let l = map head t 
                        rm = map tail t
                    in all (==0) l && triSup rm 

--5
movimenta1 :: IO (Int,Int)
movimenta1 = movimenta2 (0,0)

movimenta2 :: (Int,Int) -> IO (Int,Int)
movimenta2 (x,y) = do z <- getChar 
                      case z of 'N' -> movimenta2 (x,y+1)
                                'S' -> movimenta2  (x,y-1)
                                'E' -> movimenta2 (x+1,y)
                                'O' -> movimenta2 (x-1,y)
                                otherwise -> return (x,y)
--6
data Imagem = Quadrado Int 
            | Mover (Int,Int) Imagem 
            | Juntar [Imagem]

--a
vazia :: Imagem -> Bool 
vazia (Juntar []) = True
vazia (Quadrado x) = False 
vazia (Mover (_,_) x) = vazia x 
vazia (Juntar (x:xs)) = case x of 
    Quadrado y -> False 
    otherwise -> vazia (Juntar xs) 

--b repetir
maior :: Imagem -> Maybe Int
maior (Quadrado x) = Just x
maior (Mover (_,_) xs) = maior xs
maior (Juntar []) = Nothing  
maior (Juntar (x:xs)) | null (x:xs) = Nothing 
                      | otherwise = maximum' (filter (/= Nothing) (map maior (x:xs)))
    where maximum' [] = Nothing 
          maximum' l = maximum l

--c 
