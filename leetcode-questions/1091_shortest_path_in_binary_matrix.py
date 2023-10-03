from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        queue = deque()

        queue.append((0, 0))
        visited.add((0, 0))

        directions = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1],
            [-1, -1],
            [-1, 1],
            [1, -1],
            [1, 1],
        ]  # up,down,left,right,top-left,top-right,bottom-left,bottom-right

        clear_path = False
        length = 0
        while queue and not clear_path:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if row == ROWS - 1 and col == COLS - 1 and grid[row][col] == 0:
                    clear_path = True
                    break

                for diffR, diffC in directions:
                    newRow = row + diffR
                    newCol = col + diffC
                    if (
                        min(newRow, newCol) < 0
                        or newRow >= ROWS
                        or newCol >= COLS
                        or (newRow, newCol) in visited
                        or grid[newRow][newCol] == 1
                    ):
                        continue
                    queue.append((newRow, newCol))
                    visited.add((newRow, newCol))
            length += 1

        if length == 0 or not clear_path:
            return -1

        return length
