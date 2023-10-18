from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalSum = nums[0]

        maxSum = nums[0]
        currMaxSum = nums[0]

        minSum = nums[0]
        currMinSum = nums[0]

        for i in range(1, len(nums)):
            totalSum += nums[i]

            currMaxSum = max(currMaxSum + nums[i], nums[i])
            maxSum = max(maxSum, currMaxSum)

            currMinSum = min(currMinSum + nums[i], nums[i])
            minSum = min(minSum, currMinSum)

        if totalSum == minSum:
            return maxSum

        return max(maxSum, totalSum - minSum)


sol = Solution()
assert sol.maxSubarraySumCircular([1, -2, 3, 2]) == 6
assert sol.maxSubarraySumCircular([5, -3, 5]) == 10
assert sol.maxSubarraySumCircular([-3, -2, -3]) == -2
