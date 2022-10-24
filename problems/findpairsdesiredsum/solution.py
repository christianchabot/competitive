# O(nlog(n)) solution using sorting.
def solve(nums, val):
    nums.sort()
    left, pairs, right = 0, [], len(nums)-1
    while right > left:
        cur_sum = nums[left] + nums[right]
        if cur_sum == val:
            pairs.append((nums[left], nums[right]))
        left += int(cur_sum <= val)
        right -= int(cur_sum >= val)
    return pairs

nums = [1, 3, 6, -5, 10, 2, -3, -1]
print(solve(nums, 5))
