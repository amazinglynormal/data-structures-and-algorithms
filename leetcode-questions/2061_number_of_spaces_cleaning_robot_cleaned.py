from typing import List


class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        ans = 0

        ROWS = len(room) - 1
        COLS = len(room[0]) - 1

        visited = {}

        # right, down, left, up
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dir = 0

        curr_pos = (0, 0)

        while True:

            # add position and direction to visited
            if curr_pos in visited:
                visited_dirs = visited[curr_pos]
                visited_dirs.add(dir)
            else:
                # increase ans by 1
                ans += 1
                visited[curr_pos] = {dir}

            next_found = False

            while not next_found:

                # calculate next position
                next = (curr_pos[0] + dirs[dir][0], curr_pos[1] + dirs[dir][1])

                # check if next position has been visited with current direction if so then break
                if next in visited and dir in visited[next]:
                    return ans
                # check if next position is blocked or out of bounds, if so the turn until valid path or loop is found
                if (
                    next[0] > ROWS
                    or next[1] > COLS
                    or next[0] < 0
                    or next[1] < 0
                    or room[next[0]][next[1]] == 1
                ):
                    if dir == 3:
                        dir = 0
                    else:
                        dir += 1

                    if dir in visited[curr_pos]:
                        return ans
                    continue

                next_found = True

            # move to next position
            curr_pos = next


sol = Solution()

assert sol.numberOfCleanRooms([[0, 0, 0], [1, 1, 0], [0, 0, 0]]) == 7
assert sol.numberOfCleanRooms([[0, 1, 0], [1, 0, 0], [0, 0, 0]]) == 1
assert sol.numberOfCleanRooms([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 8
