from typing import List

# edge cases:
# length of array == 1
# all elements are equal


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        maxLength = 1

        # 0 if prev was less than & 1 if prev was greater than, -1 if equal/start
        prev = -1
        currLength = 1
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                if prev != 0:
                    currLength += 1
                else:
                    currLength = 2
                prev = 0
            elif arr[i] > arr[i - 1]:
                if prev != 1:
                    currLength += 1
                else:
                    currLength = 2
                prev = 1
            else:
                currLength = 1
                prev = -1

            if currLength > maxLength:
                maxLength = currLength

        return maxLength


sol = Solution()
assert sol.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]) == 5
assert sol.maxTurbulenceSize([4, 8, 12, 16]) == 2
assert sol.maxTurbulenceSize([100]) == 1
