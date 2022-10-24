words = input().split()

# Feel like this could be done in a one liner.
anagrams = []
for w in words:
    anagram = {w}
    words.remove(w)
    for n in words:
        if sorted(w) == sorted(n):
            anagram = anagram | {n}
            words.remove(n)
    anagrams.append(anagram)
print(anagrams)
