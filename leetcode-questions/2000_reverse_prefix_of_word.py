class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        prefix = []
        result = []

        index = 0
        while index < len(word):
            prefix.append(word[index])
            if word[index] == ch:
                while prefix:
                    result.append(prefix.pop())
                index += 1
                while index < len(word):
                    result.append(word[index])
                    index += 1
                return "".join(result)
            index += 1

        return word


sol = Solution()

assert sol.reversePrefix("abcdefd", "d") == "dcbaefd"
assert sol.reversePrefix("xyxzxe", "z") == "zxyxxe"
assert sol.reversePrefix("abcd", "z") == "abcd"
