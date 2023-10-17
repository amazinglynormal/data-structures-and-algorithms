from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        offset = 1

        for num in range(1, n + 1):
            if offset * 2 == num:
                offset = num
            ans.append(1 + ans[num - offset])

        return ans
