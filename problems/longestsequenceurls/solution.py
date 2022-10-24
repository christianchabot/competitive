def solve(user0, user1):
    i, ret = 0, []
    while i < len(user0):
        j, k, tmp = 0, i, []
        while j < len(user1) and k < len(user0):
            if user1[j] == user0[k]:
                tmp.append(user1[j])
                k += 1
            elif len(tmp) > 0 and len(tmp) > len(ret):
                k, ret, tmp = 0, tmp, []
            j += 1

        if len(tmp) > len(ret):
            ret = tmp
        i += 1
    return ret

user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

print(solve(user0, user1))
print(solve(user0, user2))
print(solve(user0, user0))
print(solve(user2, user1))
print(solve(user5, user2))
print(solve(user3, user4))
print(solve(user4, user3))
print(solve(user3, user6))
