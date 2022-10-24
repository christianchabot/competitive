
# Does not produce the optimal solution.
def solve(coins, amount):
    used = [0]*len(coins)
    for i, c in enumerate(coins[::-1]):
        for j, nc in enumerate(coins[-(i+1)::-1]):
            print(nc)
    return sum(used), tuple(used)

coins = (1, 5, 7, 9, 11)
count, used = solve(coins, 6)
#print("Amount 6 will require", count, "coins", used)
#count, used = solve(coins, 25)
#print("Amount 25 will require", count, "coins", used)
#count, used = solve(coins, 250)
#print("Amount 250 will require", count, "coins", used)

#coins = (1, 2, 5)
#count, used = solve(coins, 18)
#print("Amount 18 will require", count, "coins", used)
