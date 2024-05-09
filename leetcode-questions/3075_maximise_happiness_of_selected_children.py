# could have also used a max heap for similar time complexity

from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:

        happiness.sort(reverse=True)

        result = 0
        chosen = 0

        for i in range(k):
            val = happiness[i]
            val -= chosen
            chosen += 1
            if val < 0:
                continue
            result += val

        return result


sol = Solution()

assert sol.maximumHappinessSum([1, 2, 3], 2) == 4
assert sol.maximumHappinessSum([1, 1, 1, 1], 2) == 1
assert sol.maximumHappinessSum([2, 3, 4, 5], 1) == 5
