class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        right = 0
        currLength = 0

        used = set()

        while right < len(s):
            if s[right] in used:
                while s[right] in used:
                    used.remove(s[left])
                    left += 1
                used.add(s[right])
                currLength = right - left + 1
            else:
                used.add(s[right])

            currLength = right - left + 1
            longest = max(longest, currLength)
            right += 1

        return longest


sol = Solution()
assert sol.lengthOfLongestSubstring("abcabcbb") == 3
assert sol.lengthOfLongestSubstring("bbbbb") == 1
assert sol.lengthOfLongestSubstring("pwwkew") == 3
