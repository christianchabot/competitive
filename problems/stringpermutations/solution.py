# Heaps algorithm.
def permute(string, srt, end, out):
    if srt == end:
        out.append("".join(string))
        return

    for i in range(srt, end):
        string[srt], string[i] = string[i], string[srt]
        permute(string, srt + 1, end, out)
        string[srt], string[i] = string[i], string[srt]

string, out = input(), []
permute(list(string), 0, len(string), out)
print(out)
