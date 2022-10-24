def solve(string):
    string = list(string)
    r, l = 0, len(string)-1
    while r < l:
        rspec, lspec = int(not string[r].isalpha()), int(not string[l].isalpha())
        if rspec or lspec:
            r, l = r+rspec, l-lspec
            continue
        string[r], string[l] = string[l], string[r]
        r, l = r+1, l-1
    return str(string)

string = "abc/defgh$ij"
print(solve(string))
string = "jih/gfedc$ba"
print(solve(string))
