from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        answer = -1
        seen = set()

        for num in nums:
            negation = num * -1
            if num < 0 and negation in seen and negation > answer:
                answer = negation
            elif negation in seen and num > answer:
                answer = num
            seen.add(num)

        return answer


sol = Solution()

assert sol.findMaxK([-1, 2, -3, 3]) == 3
assert sol.findMaxK([-1, 10, 6, 7, -7, 1]) == 7
assert sol.findMaxK([-10, 8, 6, 7, -2, -3]) == -1
