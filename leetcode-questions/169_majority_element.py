from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        return max(count.keys(), key=count.get)


sol = Solution()

assert sol.majorityElement([3, 2, 3]) == 3
assert sol.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
