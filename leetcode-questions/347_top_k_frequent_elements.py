from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            curr = freq.get(num, 0)
            freq[num] = curr + 1

        sorted_freqs = sorted(freq.items(), key=lambda tup: tup[1], reverse=True)
        results = []
        for i in range(k):
            results.append(sorted_freqs[i][0])

        return results

    def leetcode_solution(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        count = Counter(nums)

        return heapq.nlargest(k, count.keys(), key=count.get)


sol = Solution()

assert sol.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
assert sol.topKFrequent([1], 1) == [1]

assert sol.leetcode_solution([1, 1, 1, 2, 2, 3], 2) == [1, 2]
assert sol.leetcode_solution([1], 1) == [1]
