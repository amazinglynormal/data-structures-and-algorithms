class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {")": "(", "]": "[", "}": "{"}

        for par in s:
            if par in mapping:
                top = stack.pop() if stack else "X"

                if mapping[par] != top:
                    return False
            else:
                stack.append(par)

        return True if len(stack) == 0 else False
