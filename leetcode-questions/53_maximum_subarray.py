from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]

        for i in range(1, len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            if currSum > maxSum:
                maxSum = currSum

        return maxSum


sol = Solution()
assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert sol.maxSubArray([1]) == 1
assert sol.maxSubArray([5, 4, -1, 7, 8]) == 23
