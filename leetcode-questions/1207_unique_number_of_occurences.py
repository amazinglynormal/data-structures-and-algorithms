from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if len(arr) == 1:
            return True

        occurrences = {}

        for num in arr:
            occurrences[num] = 1 + occurrences.get(num, 0)

        seen = set()
        for val in occurrences.values():
            if val in seen:
                return False
            seen.add(val)

        return True


sol = Solution()

assert sol.uniqueOccurrences([1, 2, 2, 1, 1, 3]) == True
assert sol.uniqueOccurrences([1, 2]) == False
assert sol.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]) == True
