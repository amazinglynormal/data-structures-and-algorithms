from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        run_one_a, run_one_b = 0, 0

        for i in range(len(nums) - 1):
            temp = max(run_one_a + nums[i], run_one_b)
            run_one_a = run_one_b
            run_one_b = temp

        run_two_a, run_two_b = 0, 0

        for j in range(1, len(nums)):
            temp = max(run_two_a + nums[j], run_two_b)
            run_two_a = run_two_b
            run_two_b = temp

        return max(run_one_b, run_two_b)


sol = Solution()
print(sol.rob([2, 3, 2]))  # 3
print(sol.rob([1, 2, 3, 1]))  # 4
print(sol.rob([1, 2, 3]))  # 3
