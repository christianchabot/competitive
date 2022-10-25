import Data.List

findPairs :: (Num a, Eq a) => [a] -> a -> [(a, a)]
findPairs [] _ = []
findPairs (_:[]) _ = []
findPairs (x:xs) v =
	if (x + s) == v then (x, s):findPairs (init xs) v
	else findPairs xs v
	where s = last xs

main = do
	let nums = findPairs (sort [1, 3, 6, -5, 10, 2, -3, -1]) 5
	print nums
