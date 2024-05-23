from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


sol = Solution()

assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert sol.search([1], 0) == -1
assert sol.search([4, 5, 6, 7, 8, 1, 2, 3], 8) == 4
