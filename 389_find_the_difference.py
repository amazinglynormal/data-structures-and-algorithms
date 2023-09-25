def findTheDifference(s: str, t: str) -> str:
    letters = {}

    for letter in s:
        if not letters.get(letter):
            letters.update({letter: 1})
        else:
            curr = letters.get(letter)
            letters.update({letter: curr + 1})

    for letter in t:
        if not letters.get(letter):
            return letter

        curr = letters.get(letter)
        if curr < 1:
            return letter

        if curr - 1 < 1:
            letters.pop(letter)
        else:
            letters.update({letter: curr - 1})
