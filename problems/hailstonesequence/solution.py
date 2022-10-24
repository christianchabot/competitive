def hailstone(n, lens):
    if n <= 1:
        return 1 # 1 assuming length is always at least 1

    if n in lens:
        return lens[n]

    start = n
    if n%2 == 0:
        n //= 2
    else:
        n = n*3 + 1

    ret = hailstone(n, lens) + 1
    lens[start] = ret
    return ret

a, b = map(int, input().split())
max_seq, seed =  0, a
lens = {}
for i in range(a, b+1):
    seq = hailstone(i, lens)
    if seq > max_seq:
        max_seq = seq
        seed = i

print("Max length of the Hailstone Sequence is %d for seed %d" % (max_seq, seed))
