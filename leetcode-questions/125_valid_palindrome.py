class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
                continue

            if not s[left].isalnum():
                left += 1
            if not s[right].isalnum():
                right -= 1

        return True


sol = Solution()

assert sol.isPalindrome("A man, a plan, a canal: Panama") == True
assert sol.isPalindrome("race a car") == False
assert sol.isPalindrome(" ") == True
