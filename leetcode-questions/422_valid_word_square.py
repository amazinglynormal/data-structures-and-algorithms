from typing import List


def validWordSquare(words: List[str]) -> bool:
    for i in range(len(words)):
        col_word = ""
        for j in range(len(words)):
            if len(words[j]) > i:
                col_word += words[j][i]

        if col_word != words[i]:
            return False
    return True


assert validWordSquare(["abcd", "bnrt", "crmy", "dtye"]) == True
assert validWordSquare(["abcd", "bnrt", "crm", "dt"]) == True
assert validWordSquare(["ball", "area", "read", "lady"]) == False
