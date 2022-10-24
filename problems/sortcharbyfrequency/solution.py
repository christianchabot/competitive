string = input()

# Count each character in O(n).
seen = {c:string.count(c) for c in string}

# Sort by counts (assuming O(nlog(n)).
sort = ""
for s, c in sorted(seen.items(), key=lambda item: item[1], reverse=True):
    sort += s*c
print(sort)
