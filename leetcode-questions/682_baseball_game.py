# operations: List[str]
# returns int
def calcPoints(operations):
    stack = []

    for op in operations:
        match op:
            case "C":
                stack.pop()
            case "+":
                stack.append(stack[-1] + stack[-2])
            case "D":
                stack.append(2 * stack[-1])
            case _:
                stack.append(int(op))

    score = 0
    for num in stack:
        score += num

    return score


operations_one = ["5", "-2", "4", "C", "D", "9", "+", "+"]
operations_two = ["5", "2", "C", "D", "+"]
operations_three = ["1", "C"]

print(calcPoints(operations_one))
print(calcPoints(operations_two))
print(calcPoints(operations_three))
