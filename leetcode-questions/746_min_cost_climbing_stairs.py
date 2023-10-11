from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minA, minB = 0, 0

        for i in range(len(cost)):
            temp = cost[i] + min(minA, minB)
            minA = minB
            minB = temp

        return min(minA, minB)


sol = Solution()
print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(sol.minCostClimbingStairs([10, 15, 20]))
