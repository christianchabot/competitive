# O(n^2) solution.
def solve(intervals=[]):
    ret = []
    if len(intervals) > 0:
        ret.append(intervals[0])
        for s, e in intervals[1:]:
            for i, (s1, e1) in enumerate(ret):
                if s >= s1 and e <= e1:
                    continue

                if s < s1 and e > e1:
                    ret[i] = (s, e)
                elif e >= s1 and e <= e1:
                    ret[i] = (s, e1)
                elif s >= s1 and s <= e1:
                    ret[i] = (s1, e)
                else:
                    ret.append((s, e))
    return ret

print(solve([(1,3), (2,6), (2,5), (8,10)]))
print(solve([]))
