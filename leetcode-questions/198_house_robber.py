from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        max1, max2 = 0, 0

        for num in nums:
            temp = max(num + max1, max2)
            max1 = max2
            max2 = temp

        return max2
