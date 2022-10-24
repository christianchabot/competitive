oper = int(input())
message = input()
key = input()

if len(message) == 0:
    quit()

i = 0
if oper == 1:
    for k in key:
        print(message[i]*int(k), end="")
        i += 1
else:
    for k in key:
        print(message[i], end="")
        i += int(k)

while i < len(message):
    print(message[i], end="")
    i += 1
print()
