# This solution counts all matching brackets.
def solve(string, depth, count):
    if string == "":
        return count

    if string[0] == "{":
        return solve(string[1:], depth+1, count)
    elif string[0] == "}":
        if depth > 0:
            return solve(string[1:], depth-1, count+2)
        else:
            return max(count, solve(string[1:], 0, 0))
    return count

print(solve("{}{}{", 0, 0))
print(solve("{}{}}", 0, 0))
print(solve("{}{{}}}}}}", 0, 0))
print(solve("{{{{}}{}}}", 0, 0))
print(solve("{}{}{}{}{}{}{}{}{}{}{}{}", 0, 0))
print(solve("{{{{}}{}}}{{{{}{}{}{}{}{}{}{}{}{}{}{}", 0, 0))
