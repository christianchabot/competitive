string, result = input(), ""
for s in string:
    if s not in result:
        result += s
print(result)
