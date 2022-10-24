pattern = input()

# Error checking (requirement by problem constraints).
if len(pattern) == 0:
    print(-1)
    quit()
for p in pattern:
    if p != 'N' and p != 'M':
        print(-1)
        quit()

# Solution
i, Mstart = 0, 0
for i, p in enumerate(pattern):
    if p == 'N':
        if Mstart > 0:
            for j in range(i + 1, Mstart - 1, -1):
                print(j, end="")
        else:
            print(i + 1, end="")
        Mstart = 0
    elif Mstart == 0:
        Mstart = i + 1

if Mstart > 0:
    for j in range(i + 2, Mstart - 1, -1):
        print(j, end="")
else:
    print(i + 2, end="")
print()

# Explanation:
# If descending in a series of Ms (take count of Ms).
# Then print the count in descending order once an N or
# the end is reached.
# Else we are ascending with Ns so just print
# the index.
