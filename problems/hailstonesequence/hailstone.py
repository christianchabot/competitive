
n = int(input())

def hailstone(n):
    while n > 1:
        print(n, end=" -> ")
        if n%2 == 0:
            n //= 2
        else:
            n = n*3 + 1
    print(n)

hailstone(n)
