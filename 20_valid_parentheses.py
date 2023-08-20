def isValid(s):
    if len(s) % 2 != 0:
        return False

    stack = []

    for bracket in s:
        match bracket:
            case ")":
                if len(stack) == 0 or stack[-1] != "(":
                    return False
                stack.pop()
            case "]":
                if len(stack) == 0 or stack[-1] != "[":
                    return False
                stack.pop()
            case "}":
                if len(stack) == 0 or stack[-1] != "{":
                    return False
                stack.pop()
            case _:
                stack.append(bracket)

    if len(stack) > 0:
        return False

    return True


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
