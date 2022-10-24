nums = [2, 3, 1, 0, 2, 5, 3]
seen = [0]*len(nums)

for n in nums:
    if seen[n] != 0:
        print(n)
        quit()
    else:
        seen[n] += 1
