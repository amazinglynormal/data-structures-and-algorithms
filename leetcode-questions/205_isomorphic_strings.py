from collections import Counter


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        replacements = {}
        used = set()
        for i in range(len(s)):
            if s[i] not in replacements and t[i] not in used:
                replacements[s[i]] = t[i]
                used.add(t[i])
            elif s[i] not in replacements and t[i] in used:
                return False
            elif replacements[s[i]] and replacements[s[i]] != t[i]:
                return False

        return True


sol = Solution()

assert sol.isIsomorphic("egg", "add") == True
assert sol.isIsomorphic("foo", "bar") == False
assert sol.isIsomorphic("paper", "title") == True
assert sol.isIsomorphic("badc", "baba") == False
