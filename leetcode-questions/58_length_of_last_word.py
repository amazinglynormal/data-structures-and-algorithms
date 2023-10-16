class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # find last valid char
        i = len(s) - 1
        while i >= 0:
            if s[i] == " ":
                i -= 1
            else:
                break

        # find start of word
        count = 0
        for j in range(i, -1, -1):
            if s[j] == " ":
                break
            count += 1

        return count
