from typing import List
import heapq


def lastStoneWeight(stones: List[int]) -> int:
    for i, num in enumerate(stones):
        stones[i] = num * -1

    heapq.heapify(stones)

    while len(stones) > 1:
        y = heapq.heappop(stones) * -1
        x = heapq.heappop(stones) * -1

        if x != y:
            y = (y - x) * -1
            heapq.heappush(stones, y)

    if len(stones) == 1:
        return stones[0] * -1

    return 0
