{-# OPTIONS_GHC -XNPlusKPatterns #-}

-- (c) Ensico & UM (2022)

module Svg where

import Data.Ratio
import Data.Char
import Data.List
import System.Process
import Cp

--- Basic -----------

open h = do { writeFile "_.html" h ; system ("open _.html") } 

converse = map swap

a .><. b = [ (x,y) | x <- a, y <- b ]

a # b = zip a b

unrstr = (id >< head) . unzip

collapse = map unrstr . transpose

match p l i = p `isPrefixOf` (drop i l)

r2 = (/100) . fromIntegral . round .(100*)

-- Generic "derivative" / "integral"

gderiv :: a -> (a -> a -> c) -> [a] -> [c]
gderiv z f s = ttl (zipWith f s (z:s))
              where ttl [] = []
                    ttl (a:t) = t

ginteg :: (a -> b -> b) -> b -> [a] -> [b]
ginteg f i s = i:aux i s
      where aux i [] = []
            aux i (h:t) = i':(aux i' t)
                          where i'=f h i

-- Repetitions

-- repeat anything 

rep x = map (const x) [0..]

-- (9) Misc.

cut :: Int -> Int -> [a] -> [a]
cut n m = (take (m-n+1)) . drop (n-1)

inds :: [b] -> [Int]
inds = (map fst) . (zip [1..])

elems :: (Ord a) => [a] -> [a]
elems = sort . nub

-- misc

sing a = [a]
dup a = [a,a]

a != b = not(a == b)

a |-> b = (a,b)

supermap f [] = []
supermap f (a:l) = a:(map f (supermap f l))

show2 = show.show

--- list of pairs to list

lp2l :: [(b, b)] -> [b]
lp2l = (concat . map f) where f(a,b)=[a,b]

frac n m = n%m

-- for combinator

for b i 0 = i
for b i (n+1) = b(for b i n)

presort f = map snd . sort . (map (split f id)) -- pre-sorting on f-preorder

apl :: [a -> b] -> [a] -> [b]
apl f l = map ap (zip f l)

--- HTML minimal API ("shallow embedding")

tag t l x = "<"++t++" "++ps++">"++x++"</"++t++">"
             where ps = unwords [concat[t,"=",v]| (t,v)<-l]

tg t l = "<"++t++" "++ps++"/>"
             where ps = unwords [concat[t,"=",v]| (t,v)<-l]

htm = tag "html" []

strong  = tag "strong" []

tr  = tag "tr" []

img fn = tag "img" [ "src" |-> (show fn) ] ""

uli = ul . (>>= li) where
    li  = tag "li" []
    ul  = tag "ul" []

htable = nest "table" [ "border" |-> "1" , "data-toggle" |-> "\"table\"" ]
             (nest "tr" [] (tag "td" [ "align" |-> "center"]))
                where nest t p f = (tag t p) . (>>=f)
                
pretty = (open . htm . htable) 

--- remove diacritics where needed

cl '\237'= 'i'
cl '\243'= 'o'
cl '\227'= 'a'
cl '\231'= 'c'
cl c     = c

--- basic -----------

mT :: Eq a => [(a, b)] -> a -> Maybe b
mT = flip lookup

pap :: Eq a => [(a, t)] -> a -> t
pap m = unJust . (mT m) where unJust (Just a) = a -- partial inspector of simple relation A->B

-- Abstract (point) level

infix 5  .|
infix 4  .+
infix 4  .-

a .| (x,y) = (a*x,a*y)

trans p = map (p .+)

(x,y) .+ (x',y') = (x+x',y+y')

(x,y) .- (x',y') = (x-x',y-y')

a .* (x,y) = (a*x,a*y)

amplia r = map (r .*)

amplia' s p = trans (p .- s .* p) . amplia s

reduz r = amplia (1/r)

-- SVG -----------------------------------

s = (200*)

sstep (x,y) = (200*x,-200*y)

scl p = sstep p .+ (-1400,1400)

shp (x,y) = show x ++ "," ++ show y  -- format for coord list

shpts xs = intercalate " " (map (shp.scl) xs) -- with offset

shpts' xs = intercalate " " (map (shp.sstep) xs)

rscale p = let (x,y) = scl p in (round x,round y)

-- paths

path d = tg "path" [ "d" |-> show d ]

slice r (p1,p2) = path $ " M " ++ shp (scl p1) ++ arc (s r) (scl p2) ++ " L " ++ shp (scl p3) where
  arc r p = " A " ++ shp (r,r) ++ " 0 0 0 " ++ shp p ++ " "
  p3 = (0,0)

-- polylines

poly xs = tg "polyline" ["points" |-> show (shpts xs), "style"  |-> show "fill:none;stroke-width:5" ]

poly' xs = tg "polyline" ["points" |-> show (shpts xs), "style"  |-> show "fill:none;stroke-width:8" ]  -- thicker

seg p q = poly [p,q]

-- polygons 

polyg xs = tg "polygon" ["points" |-> show  (shpts xs)] 

tri = polyg

squ = polyg

rect x y = polyg [(0,0),(x,0),(x,y),(0,y),(0,0)]

sqr x = rect x x

cir (x,y) r = tg "circle" [
   "cx" |-> show2 x',"cy" |-> show2 y', "r" |-> show2 r',
   "stroke" |-> show "black", "stroke-width" |-> show2 3 ] where
      (x',y') = scl (x,y)
      (r',_) = sstep (r,0)

elp (x,y) (rx,ry) = tg "ellipse" [
   "cx" |-> show2 x',"cy" |-> show2 y', "rx" |-> show2 rx', "ry" |-> show2 ry', 
   "stroke" |-> show "black", "stroke-width" |-> show2 3 ] where
      (x',y') = scl (x,y)
      (rx',_) = sstep (rx,0)
      (ry',_) = sstep (ry,0)

-- points

point p = let (x,y) = scl p in tg "circle" ["cx" |-> show2 x,"cy" |-> show2 y, "r" |-> show2 15]
point' p = tag "g" ["font-size" |-> show2 60] (point p ++ black(stext (scl (p.+(-0.5,0.2))) (shows p))) where
   shows(x,y) = "("++ s x ++ "," ++ s y ++ ")"
   s x = if abs(x-fromIntegral (round x)) < 0.001 then show (round x) else show (r2 x)

points' = (>>= point')
points = (>>= point)

-- rotation

polar (x,y) = (atan2 y x,sqrt(x^2+y^2))

cart (a,r) = (cos a * r, sin a * r) 

rad r = r*pi/180

rot r p = (x',y') where 
   (a,c) = polar p
   a' = a + rad r
   y' = c*sin a'
   x' = c*cos a'

rotate r p a = tag "g" [ "transform" |-> show ("rotate(" ++ t ++ ")") ] a where
   (x,y) = scl p
   t = unwords [show r, show x, show y]

-- translation

translate p = tag "g" [ "transform" |-> show ("translate"++p') ] where p' = show(sstep p)

put = translate

-- (static) scaling

scale k p = translate (p' .- k .* p') . 
            tag "g" ["transform" |-> show("scale(" ++ show k ++ ")") ]
                where p' = p .- (7,7)

-- colored regions

color c = tag "g" ["fill" |-> show c, "stroke" |-> show c] 
white = color "white"
black = color "black"
gray = color "gray"
yellow = color "yellow"
green = color "green"
red = color "red"
blue = color "blue"
orange = color "orange"
magenta = color "magenta"  
brown = color "brown" 

-- grouping

grp = tag "g" [] . concat

-- vectors, lines and grid

vec p q = 
   let (x1,y1) = scl p
       (x2,y2) = scl q
   in tg "line" [
         "x1" |-> show2 x1, "y1" |-> show2 y1, "x2" |-> show2 x2, "y2" |-> show2 y2,
         "stroke-width" |-> show2 8, "marker-end" |-> show "url(#arrowhead)" ]
         
-- line (x1,y1)(x2,y2) = tag "line" ["x1" |-> x1, "y1" |-> y1, "x2" |-> x2, "y2" |-> y2]

lin (x1,y1) (x2,y2) = tg "line" ["x1" |-> show2 x1, "y1" |-> show2 y1, "x2" |-> show2 x2, "y2" |-> show2 y2]


grid n = f n ++ map (sym><sym) (f n) where 
   f n = [((n,-1500),(n,1500))]
   sym (x,y) = (y,x)

-- definitions

dfs = tag "defs" [] .
      tag "marker" [ "id" |-> show "arrowhead",
                     "markerWidth" |-> show2 10,
                     "markerHeight"|-> show2 8,
                     "refX" |-> show2 9,
                     "refY" |-> show2 4,
                     "orient" |-> show "auto"] $
            tg "polygon" [ "fill" |-> show "gray", "points" |-> show "0,0 10,4 0,8" ]

-- the grid and X-Y plane

planoxy p x = wrap (dfs ++ grd ++ coords ++ axes ++  concat x)
  where
    wrap = tag "svg" [
               "width"   |-> show2 500,
               "height"  |-> show2 500,
               "viewBox" |-> show "-1500 -1500 3000 3000",
               "version" |-> show "1.1",
               "xmlns"   |-> show "http://www.w3.org/2000/svg"
               ]
    trans p = tag "g" [ "transform" |-> show ("translate"++p') ] where p' = show p
    xarrowhead = polyg [(0,-0.1),(0.3,0),(0,0.1)]
    yarrowhead = polyg [(0.1,0),(0,0.3),(-0.1,0)]
    base = let a =[0,40..1500] in a ++ map ((-1)*) a
    xs = [0..13] >>= coordx
    ys = [1..13] >>= coordy
    coordx i = stext (scl (i,-0.4)) (show i)
    coordy i = stext (scl (-0.4,i)) (show i)
    coordy' i = stext (scl (-0.55,i)) (show i)
    lx i = lin (i,-1400) (i,1400) ++ lin (-1400,i) (1400,i)
    ly i = lin (-1400,i) (1400,i)
    --- axes -------------------------------------------------
    axes = blacklines [((-1400.0,1480.0),(-1400.0,-1480.0)),((-1480.0,1400.0),(1480.0,1400.0))] ++
           trans (sstep (14.2,0)) xarrowhead ++
           trans (sstep (0,14.2)) yarrowhead ++
           tag "g" ["font-style" |-> show "italic", "font-size" |-> show2 100] (gray (
              stext (scl (14,-0.5)) "x" ++
              stext (scl (-0.5,14)) "y"
              ))
    blacklines ls = tag "g" ["stroke" |-> show "black", "stroke-width" |-> show2 5.0] (ls >>= uncurry lin)
    --- grid -------------------------------------------------
    grd = graylines (base >>= grid) ++ 
           tag "g" ["stroke" |-> show "gray", "stroke-width" |-> show2 3] ([-1400,-1200..1400] >>= lx)
    graylines ls = tag "g" ["stroke" |-> show "gray", "stroke-width" |-> show2 p] (ls >>= uncurry lin)
    --- coords -----------------------------------------------
    coords = tag "g" ["font-size" |-> show2 80] (xs ++ ys)
    ----------------------------------------------------------
   
-- Show in X-Y Cartesian plane

picd = open . htm . planoxy 0.9

picd' = open  . htm . planoxy 0  -- gray intensity = 0

picd'' = open . htm . wrap . concat

wrap = tag "svg" [
               "width"   |-> show2 500,
               "height"  |-> show2 500,
               "viewBox" |-> show "-1500 -1500 3000 3000",
               "version" |-> show "1.1",
               "xmlns"   |-> show "http://www.w3.org/2000/svg"
               ]

-- HELPER: para mostrar polygs (apenas):

polyd t =  picd [ green(polyg t) ++ points'' t ]

points'' ps = blue(points' ps) ++  red(points projs)
         where projs  = map f ps ++ map (swap.f.swap) ps
               f(x,_) = (x,0)

--- Vectors

pnt p = red (vec (0,0) p)

pnts = grp . map pnt

--- Plotting 

plt f = map (pnt f . (/10)) . take width $ [0..] where
   pnt f x = (x, f x)
   width = 142

plot = poly . plt

plot' = poly' . plt

-- Images

image fn d = tg "image" [ "href" |-> show fn, "height" |-> show2 h, "width" |-> show2 w ]
   where (w,h) = (s >< s) d

-- Animations

anima t f x = animamea x p (show t++"s") where p = take t . map f $ [0..]

anima' t d (i,n,v) x = animamea x p (show d++"s") where 
   p = map v (take m y) -- v is the "view" extracting (x,y) 
   y = ana n i
   ana n s = s : ana n (n s)
   m = sample t d

anims d f t o = translate (-7,-7) x where
   x = tag "g" [] (o' ++ st)
   f' = unwords [show f,show f]
   t' = unwords [show t,show t]
   o' = translate (7,7) o
   st = animT "0s" (show d++"s") "scale" f' t' "0"
 
animf t f a = animamea a (plt f) t  --- animation over function graph

animamea o p t = tag "g" [] (o ++ (animM (shpath p) t "0"))

shpath p = "M " ++ shpts' p ++ " " -- no way back, cf shpath p = "M " ++ shpts' p ++ " Z"

animM p d c = tg "animateMotion" [
   "path" |-> show p, 
   "dur" |-> show d, 
   "repeatCount" |-> show c
   ] 

sample :: Float -> Float -> Int
sample t d = round(d/t)

-- animd o p t = picd [ animamea o p t ]
-- path i n = i : map n (path i n)

-- Reflections

refl q p = q .+ (q .- p)

hrefl y0 p = [ (x,2*y0-y) | (x,y) <- p ]
 
vrefl x0 p = [ (2*x0-x,y) | (x,y) <- p ]


-- Rotations

animT b d k f t c = tg "animateTransform" [
   "attributeName" |-> show "transform",
   "begin" |-> show b, 
   "dur" |-> show d, 
   "type" |-> show k, 
   "from" |-> show f, 
   "to" |-> show t, 
   "repeatCount" |-> show c
   ]
   
animr d f t o = animarot o d f t 

animarot o d (f,p) (t,q) = 
   tag "g" [] (o ++ animT "0s" (show d ++ "s") "rotate" fs ts "indefinite") where
      fs = unwords [show f, show x, show y]
      ts = unwords [show t, show x', show y']
      (x,y) = scl p
      (x',y') = scl q

-- Text

txt p = tag "text" [ "x" |-> show2 x, "y" |-> show2 y, "font-size" |-> show2 100 ] where (x,y) = scl p

italic = tag "g" [ "font-style" |-> "italic" ]

anchor k = tag "g" [ "text-anchor" |-> show k ] -- k = "end"

-- Pie diagrams

mkp r ps = a # rtl a where         -- polar coordinates
    a = aux r ps
    rtl [] = []
    rtl x = tail x ++ [ head x ]
    aux r = map (cart . curry swap r . (2*pi*)) . ginteg (+) 0

dist x = map (/t) x where t = sum x -- distribution

perc x = map (/t) x where t = maximum x -- percentage 

dom = map fst
rng = map snd

pied db = picd' (pie (map snd db) ++ map f a) where
         a = colours # [1,2..] # map sh (dom db # dist(rng db))
         sh (a,n) = a ++ ": " ++ sprec n
         f((c,y),s) = ap(c, txt (1,y) s)

pie d = y where
  r = 4 -- radius
  y = map (translate (9,9) . ap) (colours # x)
  x = map (slice r) . mkp r . dist $ d

colours = [blue,green,yellow,orange,red,magenta,gray,brown,black] ++ colours 

sprec n = show (round(n*100)) ++ " %"

-- histograms in svg

histd db = picd'' $ (db' >>= bar) where 
   span db = 13 / fromIntegral(length db)
   wth db  =  9 / fromIntegral(length db)
   ylabels = (fromIntegral . maximum . map length . dom) db `min` 5
   small p = tag "text" [ "x" |-> show2 x, "y" |-> show2 y, "font-size" |-> show2 80 ] where (x,y) = scl p
   r = map fromIntegral (rng db)
   db'=sort $ db # (perc r # [ span db * fromIntegral i | i <- [1..]] )
   bar ((s,v),(p,x)) =
          [ (brown . translate (x-w/2,y0)) (rect w y),
            (blue  . rotate 90 (x,y0-0.5) . txt (x,y0-0.5)) s,
            (gray  . anchor "middle" . small (x,y0+y + 0.2 ) . show) v
          ] where y  = p*(12-y0)
                  w  = wth db
                  y0 = ylabels

stext (x,y) = tag "text" [ "x" |-> show2 x, "y" |-> show2 y ]  -- simple text


text x y t = tag "text" [ "x" |-> show2 x, "y" |-> show2 y, "dy" |-> show "0.35em", "font-size" |-> show2 5] t

title t s = tag "title" ["id" |-> show "title"] t ++ s

bar s (y,(a,n)) = tag "g" [ "class" |-> show "bar", "transform" |-> show ("translate(0,"++show y++")") ]
      $ aux (a,n) where
        s' n = s (fromIntegral n)
        aux (t,x) = rect (s' x) ++
                    tag "text" [ "x" |-> show2 (s' x+5),
                                 "y" |-> show2 7.5,
                                 "dy" |-> show "0.30em"] (t ++ " [ " ++ show (x) ++ " ]")
        rect x  = tag "rect" [ "width" |-> show2 x, "height" |-> show2 10, "style" |-> show "fill:rgb(185,181,180);stroke-width:1;stroke:rgb(256,256,256)"] ""

fdiv :: Int -> Int -> Float
fdiv n m = fromIntegral n / fromIntegral m

svg' x y = tag "svg" 
     [ "version" |-> show "1.1",
       "xmlns" |-> show "http://www.w3.org/2000/svg",
       "xmlns:xlink" |-> show "http://www.w3.org/1999/xlink",
       "class" |-> show "chart",
       "width" |-> show2 1000,
       "height" |-> show2 (y * 24),
       "aria-labelledby" |-> show "title",
       "role" |-> show "img"
     ]

------ SETS AND FUNCTIONS

src (x,y) t = grp [
       red (point (x,y)),
       blue (end (txt (x-0.29,y-0.15) t)) 
       ] where end = anchor "end"
       
dst (x,y) t = grp [
       red (point (x,y)),
       blue (txt (x+0.29,y-0.15) t)
       ]
       
ffdAux ff = (map (g><id) a,map (h><id) (converse b),[(g i,h(f i)) | i <- map fst a ]) where
  a = zip [1..] l
  b = zip r [1..]
  f = pap b . pap ff . pap a
  (l,r) = (nub >< nub) . unzip $ ff
  g y = (5,y)
  h y = (9,y)

bold = tag "g" [ "font-weight" |-> show "bold" ]
  
container n c x a = grp [
   c (elp (x, (m+1)/2) (2,m')), 
   (red . center . bold) (txt (x,m + 2) n)
   ] where m = fromIntegral (length a)
           m' = 0.6 * m
           center = anchor "middle"

-- diagrams of functions

fund f = ffd (graph f [minBound .. maxBound])

ffd ff na nb = picd'' . singl . (translate (0,3)) . scale 1 (0,0) . grp $ 
     [ container na yellow 4 a,
       container nb orange 10 b, 
       gray (p >>= uncurry vec), 
       a >>= uncurry src,
       b >>= uncurry dst
     ] where (a,b,p) = ffdAux ff

graph f = map (split show (show.f))

graph' f = map (split show f) 

mhd f = histd (graph' f [minBound .. maxBound]) -- measure histograms

---
