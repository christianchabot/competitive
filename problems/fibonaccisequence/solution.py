n = int(input())

x, y = 0, 1
if n > 0:
    print("[%d" % x, end="")
    for i in range(1, n):
        x, y = y, x+y
        print(", %d" % x, end="")
    print("]", end="")
print()
