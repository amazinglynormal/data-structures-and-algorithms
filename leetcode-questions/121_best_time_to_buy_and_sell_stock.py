from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("inf")
        maxProfit = 0

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice

        return maxProfit


sol = Solution()
assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
