class minStack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append([val, val])
        else:
            curr_min = self.stack[-1][1]
            if val <= curr_min:
                self.stack.append([val, val])
            else:
                self.stack.append([val, curr_min])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[-1][1]
