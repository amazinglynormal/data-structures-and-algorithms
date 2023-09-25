from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    nums_checked = {}
    for idx, num in enumerate(nums):
        needed = target - num
        if needed in nums_checked:
            return [nums_checked.get(needed), idx]

        nums_checked[num] = idx
