class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        upper = x // 2
        lower = 2

        while lower <= upper:
            mid = (lower + upper) // 2
            num = mid * mid
            if num == x:
                return mid
            if num > x:
                upper = mid - 1
            else:
                lower = mid + 1

        return upper


sol = Solution()

assert sol.mySqrt(4) == 2
assert sol.mySqrt(8) == 2
assert sol.mySqrt(1024) == 32
assert sol.mySqrt(8192) == 90
