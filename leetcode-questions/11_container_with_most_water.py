from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        ans = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            ans = max(area, ans)

            if height[right] < height[left]:
                right -= 1
            else:
                left += 1

        return ans


sol = Solution()

assert sol.maxArea([1, 1]) == 1
assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert sol.maxArea([2, 3, 4, 5, 18, 17, 6]) == 17
