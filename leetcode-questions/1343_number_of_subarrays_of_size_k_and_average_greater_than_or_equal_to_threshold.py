from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0

        result = 0

        subarray = sum(arr[0:k])
        if subarray // k >= threshold:
            result += 1

        for i in range(k, len(arr)):
            subarray -= arr[i - k]
            subarray += arr[i]
            if subarray // k >= threshold:
                result += 1

        return result


sol = Solution()
assert sol.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4) == 3
assert sol.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5) == 6
