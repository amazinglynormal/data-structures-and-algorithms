from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = arr[-1]

        for i in range(len(arr) - 2, -1, -1):
            val = arr[i]
            arr[i] = greatest
            if val > greatest:
                greatest = val
        arr[-1] = -1
        return arr
