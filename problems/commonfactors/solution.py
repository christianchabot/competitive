a, b = map(int, input().split())

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return max(a, -a)

i, count = 2, 1
while i <= gcd(a, b):
    if a % i == 0 and b % i == 0:
        count += 1
    i += 1

print(count)
