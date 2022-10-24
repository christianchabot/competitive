nums = [2, 4, 5, 1, 2, 3]

# O(n) + O(n) solution.
left, right = nums[0], sum(nums[1:])
global i
for i, n in enumerate(nums[1:], start=1):
    right -= n
    if right == left:
        print(i)
        break
    left += n
