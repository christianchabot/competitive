nums = [2, 4, 3, 6, 3, 2, 5, 5]

# Take Xor to cancel the duplicates.
xor = 0
for n in nums:
    xor ^= n

if len(nums) % 2 != 0:
    print(xor)
    quit()

# Find the first bit that is different between the 2 numbers.
global i
for i, bit in enumerate(bin(xor)[::-1]):
    if bit == '1':
        break

# One group has bit and the other group does not.
groups = [0]*2
for n in nums:
    groups[bool((1 << i) & n)] ^= n

print("%d\n%d" % (groups[0], groups[1]))
