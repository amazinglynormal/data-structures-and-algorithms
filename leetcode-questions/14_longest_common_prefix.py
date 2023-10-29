from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""

        matching = True

        i = 0

        while matching and i < len(strs[0]):
            char = strs[0][i]

            for str in strs:
                if i >= len(str):
                    matching = False
                    break

                if str[i] == char:
                    continue

                matching = False

            if matching:
                longest_prefix += char
                i += 1

        return longest_prefix


sol = Solution()

assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""
