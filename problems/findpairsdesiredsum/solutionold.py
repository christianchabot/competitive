# O(n^2) Solution
def solve(nums, val):
    return list({(n, m) if n < m else (m, n) for n in nums for m in nums[1:] if n+m == val})

nums = [1, 3, 6, -5, 10, 2, -3, -1] # Assume no duplicates.
print(solve(nums, 5))
