def solve(stream):
    ret, stack = "", []
    for s in stream:
        if s not in stack:
            stack.append(s)
        else:
            stack.remove(s)
        ret += stack[0]
    return ret

streams = ["abcdabc", "csestacklearnprogrammingpractically"]
for s in streams:
    print(solve(s))
