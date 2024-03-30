class TwoSum:

    def __init__(self):
        self.arr = []
        

    def add(self, number: int) -> None:
        self.arr.append(number)
        

    def find(self, value: int) -> bool:
        seen = set()
        for num in self.arr:
            if value - num in seen:
                return True
            seen.add(num)
        return False