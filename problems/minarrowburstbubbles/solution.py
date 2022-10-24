heights = list(map(int, input().split()))

count = 0
for i, h in enumerate(heights):
    if h < 0:
        continue

    arrow = h
    for j, n in enumerate(heights[i:], start=i):
        if n >= 0 and n == arrow:
            heights[j] = -1
            arrow -= 1
    count += 1
print(count)
