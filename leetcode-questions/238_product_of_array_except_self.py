from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        prefix = []
        suffix = [0] * len(nums)

        j = len(nums) - 1
        pre = 1
        suf = 1
        for i in range(len(nums)):
            pre *= nums[i]
            suf *= nums[j]
            prefix.append(pre)
            suffix[j] = suf
            j -= 1

        for i in range(len(nums)):
            left = prefix[i - 1] if i > 0 else 1
            right = suffix[i + 1] if i < len(nums) - 1 else 1
            answer.append(left * right)

        return answer
