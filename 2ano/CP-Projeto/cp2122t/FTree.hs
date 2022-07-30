{-# OPTIONS_GHC -XNPlusKPatterns #-}

-- (c) MP-I (1998/9-2006/7) and CP (2005/6-2021/22)

module FTree where

import Cp

-- (1) Datatype definition -----------------------------------------------------

data FTree a c = Unit c | Comp a (FTree a c, FTree a c) deriving Show

inFTree = either Unit (uncurry Comp)

outFTree (Unit c)         = Left c
outFTree (Comp a (t1,t2)) = Right(a,(t1,t2))

baseFTree f g h  = f -|- (g  >< (h >< h))

-- (2) Ana + cata + hylo -------------------------------------------------------

recFTree f = baseFTree id id f

cataFTree a = a . (recFTree (cataFTree a)) . outFTree

anaFTree f = inFTree . (recFTree (anaFTree f) ) . f

hyloFTree a c = cataFTree a . anaFTree c

-- (3) Map ---------------------------------------------------------------------

instance BiFunctor FTree
         where bmap f g = cataFTree ( inFTree . baseFTree g f id )

-- (4) Examples ----------------------------------------------------------------

-- (4.1) Inversion (mirror) ----------------------------------------------------

invFTree = cataFTree (inFTree . (id -|- id >< swap))

-- (4.2) Counting --------------------------------------------------------------

countFTree = cataFTree (either (const 1) (succ . (uncurry (+)) . p2))

-- (4.3) Flattening ------------------------------------------------------------

flatFTree = cataFTree flt

flt = either singl (cons.(id><conc))

-- (4.4) Generating lists of Booleans ------------------------------------------

genBoolTree = anaFTree gbt

gbt = f where
   f(0,x)=i1 x
   f(n+1,x) = i2(x,((n,False:x),(n,True:x)))

genBools = hyloFTree flt gbt

