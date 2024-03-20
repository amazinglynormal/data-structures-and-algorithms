class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) == 0:
            return word2
        if len(word2) == 0:
            return word1

        mergedStr = ""

        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            mergedStr = mergedStr + word1[i]
            mergedStr = mergedStr + word2[j]
            i = i + 1
            j = j + 1

        while i < len(word1):
            mergedStr = mergedStr + word1[i]
            i = i + 1

        while j < len(word2):
            mergedStr = mergedStr + word2[j]
            j = j + 1

        return mergedStr