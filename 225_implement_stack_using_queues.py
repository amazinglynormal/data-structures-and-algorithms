from queue import Queue


class MyStack:
    def __init__(self):
        self.stack = Queue()

    def push(self, x: int) -> None:
        self.stack.put(x)
        for _ in range(self.stack.qsize() - 1):
            top = self.stack.get()
            self.stack.put(top)

    def pop(self) -> int:
        return self.stack.get()

    def top(self) -> int:
        top = self.stack.get()
        self.push(top)
        return top

    def empty(self) -> bool:
        return self.stack.empty()
