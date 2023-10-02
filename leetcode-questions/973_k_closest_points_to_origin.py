from typing import List
import math
import heapq


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    closest_points = []

    for point in points:
        dist = math.dist(point, [0, 0])
        heapq.heappush(closest_points, (dist, point))

    result = []

    for _ in range(k):
        point = heapq.heappop(closest_points)
        result.append(point[1])

    return result
