t = int(input())
nums = [int(input()) for x in range(1, t+1)]

for n in nums:
    prod, sum = 1, 0
    for i in range(1, n+1):
        prod *= i
        sum += i
    if prod%sum == 0:
        print("YEAH")
    else:
        print("NAH")
