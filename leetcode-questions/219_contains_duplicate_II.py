from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False

        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in seen and abs(seen[num] - i) <= k:
                return True
            else:
                seen[num] = i

        return False


sol = Solution()

assert sol.containsNearbyDuplicate([1, 2, 3, 1], 3) == True
assert sol.containsNearbyDuplicate([1, 0, 1, 1], 1) == True
assert sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False
