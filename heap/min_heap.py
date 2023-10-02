from typing import List


class min_heap:
    def __init__(self):
        self.heap = [-1]

    def push(self, val: int) -> None:
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

    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1

        if len(self.heap) == 2:
            return self.heap.pop()

        self.__swap(1, -1)

        min = self.heap.pop()

        # while left child exists
        i = 1
        while i * 2 < len(self.heap):
            child = i * 2

            # if right child exists and is smaller than left
            if child + 1 < len(self.heap) and self.heap[child] > self.heap[child + 1]:
                child += 1

            # if larger than parent, no more swapping is required
            if self.heap[child] >= self.heap[i]:
                break

            self.__swap(i, child)
            i = child

        return min

    def top(self) -> int:
        return self.heap[1] if len(self.heap) >= 2 else -1

    def heapify(self, list: List[int]) -> None:
        for val in list:
            self.push(val)

    def __swap(self, i, j) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


heap = min_heap()
print(heap.top())
heap.push(7)
heap.push(9)
heap.push(8)
print(heap.top())
print(heap.pop())
print(heap.top())
print(heap.pop())
print(heap.top())
print(heap.pop())
print(heap.top())
heap.heapify([1, 2, 3, 4, 5])
print(heap.top())
print(heap.pop())
print(heap.top())
print(heap.pop())
print(heap.top())
print(heap.pop())
print(heap.top())
print(heap.pop())
print(heap.top())
print(heap.pop())
print(heap.pop())
