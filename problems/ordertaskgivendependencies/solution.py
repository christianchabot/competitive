def solve(pack_count, deps):
    pack, ret = [[] for i in range(pack_count)], []

    # Greedy:
    #    Add the dependency to the list in front.

    for i, j in deps:
        pack[j].append(i)
    return pack

dependencies = [(2, 0), (1, 2), (3, 1), (3, 2)]
print(solve(4, dependencies))
