from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums) + 1
        total = 0
        left = 0

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                length = min(length, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if length == len(nums) + 1 else length


sol = Solution()

assert sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
assert sol.minSubArrayLen(4, [1, 4, 4]) == 1
assert sol.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
