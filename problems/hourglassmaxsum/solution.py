array = [
    [1,1,1,0,0,0],
    [0,1,0,0,0,0],
    [1,1,1,0,0,0],
    [0,0,2,4,4,0],
    [0,0,0,2,0,0],
    [0,0,1,2,4,0]
]

array2 = [
    [1,1,1],
    [0,1,0],
    [1,1,1]
]

array3 = [
    [1,1,0],
    [0,1,0],
    [1,1,1]
]

array4 = [
    [1,1],
    [0,1],
    [1,1]
]

def solve(array):
    max = 0
    for i in range(0, len(array)-2):
        for j in range(0, len(array[i])-2):
            if (array[i][j] > 0 and array[i][j+1] > 0 and array[i][j+2] and
                array[i+1][j+1] > 0 and array[i+2][j] > 0 and array[i+2][j+1] and
                array[i+2][j+2] > 0):
                total = sum(array[i][j:j+3]) + array[i+1][j+1] + sum(array[i+2][j:j+3])
                if total > max:
                    max = total
    return max
print(solve(array))
print(solve(array2))
print(solve(array3))
print(solve(array4))
