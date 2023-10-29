from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1

        while L < R:
            sum = numbers[L] + numbers[R]
            if sum > target:
                R -= 1
            elif sum < target:
                L += 1
            else:
                return [L + 1, R + 1]


sol = Solution()
assert sol.twoSum([2, 7, 11, 15], 9) == [1, 2]
assert sol.twoSum([2, 3, 4], 6) == [1, 3]
assert sol.twoSum([-1, 0], -1) == [1, 2]
