from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans


sol = Solution()

assert sol.buildArray([0, 2, 1, 5, 3, 4]) == [0, 1, 2, 4, 5, 3]
assert sol.buildArray([5, 0, 1, 2, 3, 4]) == [4, 5, 0, 1, 2, 3]
