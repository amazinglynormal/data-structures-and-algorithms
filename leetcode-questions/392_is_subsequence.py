class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0
        for letter in s:
            idx = t.find(letter, start)
            if idx == -1:
                return False
            start = idx + 1

        return True


sol = Solution()
print(sol.isSubsequence("abc", "ahbgdc"))  # True
print(sol.isSubsequence("axc", "ahbgdc"))  # False
print(sol.isSubsequence("acb", "ahbgdc"))  # False
print(sol.isSubsequence("acbb", "acb"))  # False
