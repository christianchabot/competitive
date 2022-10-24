# Print using tree like structure?
# Every left parens needs a right.
# O(n!)
def solve(n):
    # Generate perms and print
    for i in range(n):
        print('(', end="")
    print()

solve(1)
solve(2)
solve(3)
