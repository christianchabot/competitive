nums = [2, 4, 5, 1, 2, 3]

# O(n) solution (using a pivot point).
l, lsum = 0, nums[0]
r, rsum = len(nums) - 1, nums[len(nums) - 1]
while l < r:
    if lsum == rsum and l + 2 == r:
        print(l + 1)
        break
    elif lsum < rsum:
        l += 1
        lsum += nums[l]
    else:
        r -= 1
        rsum += nums[r]
