def solve(array, val):
    def recurse(array, low, high):
        nonlocal val
        if low >= high:
            return -1
        mid = (low+high)//2
        if array[mid] == val:
            return mid
        elif array[mid] < val:
            return recurse(array, mid+1, high)
        else:
            return recurse(array, low, mid-1)
    return recurse(array, 0, len(array))

array = [1, 2, 3, 7, 9, 10, 15, 20, 28, 30, 500]
print(solve(array, 15))
print(solve(array, 17))
print(solve(array, 500))
