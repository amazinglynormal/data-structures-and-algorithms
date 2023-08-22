from collections import deque


def countStudents(students, sandwiches) -> int:
    top_of_stack = 0
    q = deque()

    for std in students:
        q.append(std)

    cycle = False

    while not cycle:
        cycle = True
        q.append(-1)
        std = q.popleft()
        while std != -1:
            if std == sandwiches[top_of_stack]:
                top_of_stack += 1
                cycle = False
            else:
                q.append(std)

            if len(q) > 0:
                std = q.popleft()

    return len(q)


print(countStudents([1, 1, 0, 0], [0, 1, 0, 1]))  # should return 0
print(countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))  # should return 3
