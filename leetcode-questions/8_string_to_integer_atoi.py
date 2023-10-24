class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0

        UPPER_LIMIT = 2147483647
        LOWER_LIMIT = -2147483648

        result = 0
        sign = 1

        i = 0
        while i < len(s) and s[i] == " ":
            i += 1

        if i < len(s) and s[i] == "+":
            i += 1
        elif i < len(s) and s[i] == "-":
            sign = -1
            i += 1

        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            result = 10 * result + digit
            i += 1

        if result * sign > UPPER_LIMIT:
            return UPPER_LIMIT

        if result * sign < LOWER_LIMIT:
            return LOWER_LIMIT

        return result * sign


sol = Solution()
assert sol.myAtoi("42") == 42
assert sol.myAtoi("    -42") == -42
assert sol.myAtoi("4193 with words") == 4193
assert sol.myAtoi("010") == 10
