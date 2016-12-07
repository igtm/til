{-# OPTIONS -Wall -Werror #-}

{- 複製 -}
replicate'::Int -> a -> [a]
replicate' cnt val
  | cnt <= 0 = []
  | otherwise = val: replicate' (cnt-1) val

{- リストの最初から指定数番目のリストを取得 -}
take'::Int -> [a] -> [a]
take' n _
  | n <= 0 = []
take' _ [] = []
take' n (x:ls) = x: take' (n-1) ls

{- 逆順リスト -}
reverse'::[a] -> [a]
reverse' [] = []
reverse' (x:xs) = (reverse' xs) ++ [x]

{- 無限リスト -}
repeat'::a -> [a]
repeat' x = x : repeat' x

{- ２つのリストから、１つのタプルリストを作成 -}
zip'::[a] -> [b] -> [(a,b)]
zip' _ [] = []
zip' [] _ = []
zip' (x:xs) (y:ys) = (x,y) :  zip' xs ys

{- findみたいなもの -}
elem'::(Eq a) => a -> [a] -> Bool
elem' _ [] = False 
elem' x (y:ys)
  | x == y = True
  |otherwise = elem' x ys