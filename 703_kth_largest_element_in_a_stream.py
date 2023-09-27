from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [-1]
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        idx = len(self.heap)
        self.heap.append(val)

        parent = idx // 2

        while parent >= 1:
            if self.heap[idx] < self.heap[parent]:
                self.__swap(idx, parent)
                idx = parent
                parent = idx // 2
            else:
                break

        while len(self.heap) > self.k + 1:
            self.__pop()

        return self.heap[1]

    def __pop(self) -> None:
        self.__swap(1, -1)

        self.heap.pop()

        i = 1

        while i * 2 < len(self.heap):
            child = i * 2
            if child + 1 < len(self.heap) and self.heap[child] > self.heap[child + 1]:
                child += 1

            if self.heap[child] >= self.heap[i]:
                break

            self.__swap(i, child)
            i = child

    def __swap(self, i, j) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


heap = KthLargest(3, [4, 5, 8, 2])
print(heap.add(3))
print(heap.add(5))
print(heap.add(10))
print(heap.add(9))
print(heap.add(4))
