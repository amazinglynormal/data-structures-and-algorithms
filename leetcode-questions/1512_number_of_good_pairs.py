from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        table = {}
        good_pairs = 0

        for num in nums:
            curr = table.get(num, 0)
            good_pairs += curr
            table[num] = curr + 1

        return good_pairs


sol = Solution()

assert sol.numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4
assert sol.numIdenticalPairs([1, 1, 1, 1]) == 6
assert sol.numIdenticalPairs([1, 2, 3]) == 0
