from typing import List


def transformArray(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr

    changes_made = True

    copy = arr[:]
    while changes_made:
        changes = [copy[0]]
        changes_made = False

        for i in range(1, len(copy) - 1):

            curr = copy[i]
            if curr < copy[i - 1] and curr < copy[i + 1]:
                changes.append(curr + 1)
                changes_made = True
            elif curr > copy[i - 1] and curr > copy[i + 1]:
                changes.append(curr - 1)
                changes_made = True
            else:
                changes.append(curr)

        changes.append(copy[-1])
        copy = changes

    return copy


assert transformArray([6, 2, 3, 4]) == [6, 3, 3, 4]
assert transformArray([1, 6, 3, 4, 3, 5]) == [1, 4, 4, 4, 4, 5]
assert transformArray([1]) == [1]
assert transformArray([1, 2]) == [1, 2]
assert transformArray([1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1]
assert transformArray([2, 1, 2, 1, 1, 2, 2, 1]) == [2, 2, 1, 1, 1, 2, 2, 1]
