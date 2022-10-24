def solve(array, val):
    low, high, = 0, len(array)
    while low < high:
        mid = (low+high)//2
        if array[mid] == val:
            return mid
        elif array[mid] < val:
            low = mid+1
        else:
            high = mid-1
    return -1

array = [1, 2, 3, 7, 9, 10, 15, 20, 28, 30, 500]
print(solve(array, 15))
print(solve(array, 17))
print(solve(array, 500))
