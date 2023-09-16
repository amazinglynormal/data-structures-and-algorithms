def searchMatrix(matrix, target: int) -> bool:
    row = -1

    topRow = 0
    bottomRow = len(matrix) - 1

    while topRow <= bottomRow:
        midRow = (topRow + bottomRow) // 2

        if matrix[midRow][0] <= target <= matrix[midRow][-1]:
            row = midRow
            break
        elif target < matrix[midRow][0]:
            bottomRow = midRow - 1
        else:
            topRow = midRow + 1

    if row == -1:
        return False

    l = 0
    r = len(matrix[row]) - 1

    while l <= r:
        mid = (l + r) // 2
        val = matrix[row][mid]

        if target == val:
            return True
        elif target < val:
            r = mid - 1
        else:
            l = mid + 1

    return False


print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))  # True
print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))  # False
print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 22))  # False
print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60))  # True
