
invalid_sudoku = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,8]
]
invalid_sudoku2 = [
    [1,2,3,4,5,6,7,8,9],
    [2,3,4,5,6,7,8,9,1],
    [3,4,5,6,7,8,9,1,2],
    [4,5,6,7,8,9,1,2,3],
    [5,6,7,8,9,1,2,3,4],
    [6,7,8,9,1,2,3,4,5],
    [7,8,9,1,2,3,4,5,6],
    [8,9,1,2,3,4,5,6,7],
    [9,1,2,3,4,5,6,7,8]
]
valid_sudoku = [
    [1,4,5,3,2,7,6,9,8],
    [8,3,9,6,5,4,1,2,7],
    [6,7,2,9,1,8,5,4,3],
    [4,9,6,1,8,5,3,7,2],
    [2,1,8,4,7,3,9,5,6],
    [7,5,3,2,9,6,4,8,1],
    [3,6,7,5,4,2,8,1,9],
    [9,8,4,7,6,1,2,3,5],
    [5,2,1,8,3,9,7,6,4]
]

# Iterate over the array and check for duplicates in rows and columns.
# If no duplicates in rows/columns there is exactly 9 of each number
# then it is a valid sudoku.
def solve(sudoku):
    total = [0]*9
    for i, row in enumerate(sudoku):
        row_seen = [0]*9
        if len(set(row)) != 9:
            return False

        # Check columns and squares using bitmap.
        col_seen, square_seen = 0, 0
        for j in range(9):
            col_seen |= 1 << sudoku[j][i] - 1
            square_seen |= 1 << sudoku[i%3*3 + j//3][j%3] - 1

        if col_seen != 0x1ff or square_seen != 0x1ff:
            return False
    return True

sudokus = [invalid_sudoku, invalid_sudoku2, valid_sudoku]
for s in sudokus:
    if solve(s):
        print("Sudoku is valid.")
    else:
        print("Sudoku is not valid.")
