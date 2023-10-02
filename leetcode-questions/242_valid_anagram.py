def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    letters = {}

    for letter in s:
        if not letters.get(letter):
            letters.update({letter: 1})
        else:
            curr = letters.get(letter)
            letters.update({letter: curr + 1})

    for letter in t:
        if not letters.get(letter):
            return False

        curr = letters.get(letter)
        if curr < 1:
            return False

        if curr - 1 < 1:
            letters.pop(letter)
        else:
            letters.update({letter: curr - 1})

    if len(letters.keys()) > 0:
        return False

    return True
