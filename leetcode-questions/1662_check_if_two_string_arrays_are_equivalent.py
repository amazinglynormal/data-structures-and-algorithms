from typing import List


def arrayStringAreEqual(word1: List[str], word2: List[str]) -> bool:
    ptr1 = 0
    ptr1_char = 0
    ptr2 = 0
    ptr2_char = 0

    while ptr1 < len(word1) and ptr2 < len(word2):

        if word1[ptr1][ptr1_char] != word2[ptr2][ptr2_char]:
            return False

        ptr1_char += 1
        ptr2_char += 1

        if ptr1_char >= len(word1[ptr1]):
            ptr1 += 1
            ptr1_char = 0

        if ptr2_char >= len(word2[ptr2]):
            ptr2 += 1
            ptr2_char = 0

    if ptr1 == len(word1) and ptr2 == len(word2):
        return True

    return False


assert arrayStringAreEqual(["ab", "c"], ["a", "bc"]) == True
assert arrayStringAreEqual(["a", "cb"], ["ab", "c"]) == False
assert arrayStringAreEqual(["abc", "d", "defg"], ["abcddefg"]) == True
