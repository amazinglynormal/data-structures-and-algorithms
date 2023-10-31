from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                leftEmpty = (i == 0) or (flowerbed[i - 1] == 0)
                rightEmpty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if leftEmpty and rightEmpty:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        return count >= n


sol = Solution()

assert sol.canPlaceFlowers([1, 0, 0, 0, 1], 1) == True
assert sol.canPlaceFlowers([1, 0, 0, 0, 1], 2) == False
assert sol.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2) == False
