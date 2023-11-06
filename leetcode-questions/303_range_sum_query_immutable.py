from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefixes = self.__calc_prefixes(nums)

    def sumRange(self, left: int, right: int) -> int:
        minus = self.prefixes[left - 1] if left > 0 else 0
        return self.prefixes[right] - minus

    def __calc_prefixes(self, nums: List[int]) -> List[int]:
        prefixes = []

        for i in range(len(nums)):
            prev = prefixes[i - 1] if i > 0 else 0
            prefixes.append(nums[i] + prev)

        return prefixes
