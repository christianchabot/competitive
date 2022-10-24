def solve(arr, n, k):
    result, i = 0, 0
    while i < n:
        if i > k:
            continue

        count = 0
        is_sub = False
        while i < n and arr[i] <= k:
            count += 1
            if arr[i] == k:
                is_sub = True
            i += 1

        if is_sub:
            result += count
        i += 1
    return result

t = int(input())
for i in range(1, t+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(arr, n, k))
