class Solution:
    def reverseBits(self, n: int) -> int:
        num = 0

        for i in range(32):
            bit = (n >> i) & 1
            num = num | (bit << 31 - i)
        return num


sol = Solution()
print(sol.reverseBits(1200))
print(sol.reverseBits(12))
