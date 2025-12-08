def scoreOfString(s: str) -> int:
    score = 0
    i = 0
    j = 1
    while j < len(s):
        score += abs(ord(s[i]) - ord(s[j]))
        i += 1
        j += 1

    return score
