# Does not produce the optimal solution.
def solve(coins, amount):
    used = [[0]*amount]*len(coins)
    for i, c in enumerate(coins[::-1]):
        for j, nc in enumerate(coins[-(i+1)::-1]):
            print(nc)
    return sum(used), tuple(used)

coins = (1, 5, 7, 9, 11)
count, used = solve(coins, 25) # Should return 3 coins.
