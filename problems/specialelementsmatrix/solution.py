# Check the min and max for both row and columns in the diagonal.
# Work in a diagonal on row and columns until the end is reached.
# Continue on the remaining row or columns if not a square matrix.

def solve(m, n, mat):
    r, c, count = 0, 0, 0
    special = set()

    # Calculate values on diagonal.
    while r < m and c < n:
        # Check row.
        rmin, rmax = float('inf'), -1
        for i in mat[r]:
            if i == rmin or i == rmax:
                return -1
            if i < rmin:
                rmin = i
            if i > rmax:
                rmax = i

        # Check column.
        cmin, cmax, = float('inf'), -1
        j = 0
        while j < n:
            if mat[j][c] == cmin or mat[j][c] == cmax:
                return -1
            if mat[j][c] < cmin:
                cmin = mat[j][c]
            if mat[j][c] > cmax:
                cmax = mat[j][c]
            j += 1

        # Add up all the special values.
        special = special | {rmin, rmax, cmin, cmax}
        r, c = (r + 1, c + 1)

    # Iterate on remaining rows.
    # Iterate on remaining columns.

    return len(special)

m, n = 3, 3
mat = [[1, 3, 4], [5, 2, 9], [8, 7, 6]]
print(solve(m, n, mat))
