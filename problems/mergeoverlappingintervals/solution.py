# O(nlog(n)).
def solve(intervals=[]):
    intervals = sorted(intervals)
    for i, (s, e) in enumerate(intervals[:-1]):
        for (s1, e1) in intervals[1:]:
            if s >= s1 and e <= e1:
                intervals.remove((s1, e1))
            elif s1 >= s and s1 <= e:
                intervals.remove((s1, e1))
                intervals[i] = (s, e1)
            elif e1 >= s and e1 <= e:
                intervals.remove((s1, e1))
                intervals[i] = (s, e1)
    return intervals

print(solve([(1,3), (2,6), (2, 5), (8,10)]))
print(solve([]))
