#prices = list(map(int, input().split()))

prices = [100, 180, 260, 310, 40, 535, 695]

bought = False
profit = 0 # Figure out how to print the profit gained.
for i in range(1, len(prices)-1):
    if prices[i - 1] < prices[i]:
        if not bought:
            bought = True
            print("Buy stock on day %d (%d)" % (i, prices[i - 1]))
    else:
        if bought:
            print("Sell stock on day %d (%d)" % (i, prices[i - 1]))
            bought = False

if bought:
    print("Sell stock on day %d (%d)" % ((i + 2), prices[i + 1]))
