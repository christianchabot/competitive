
# Given solution which is not correct.
def solve(string):
    count, count_list, stack = 0, [], []
    for ch in string:
        if ch ==  "{":
            stack.append(ch)
        elif len(stack) > 0:
            count += 1
            stack.pop()
        else:
            count_list.append(count) 
            count = 0
    count_list.append(count)
    return max(count_list)*2

print(solve("{}{}{"))
print(solve("{}{}}"))
print(solve("{}{{}}}}}}"))
print(solve("{{{{}}{}}}"))
print(solve("{}{}{}{}{}{}{}{}{}{}{}{}"))
print(solve("{{{{}}{}}}{{{{}{}{}{}{}{}{}{}{}{}{}{}"))
