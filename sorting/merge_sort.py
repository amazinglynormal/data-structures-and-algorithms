def merge_sort(arr, start, end):
    # checks if len(arr) is 1 as
    # a single element is always sorted
    if end - start + 1 <= 1:
        return arr

    middle = (start + end) // 2

    merge_sort(arr, start, middle)
    merge_sort(arr, middle + 1, end)

    merge(arr, start, middle, end)

    return arr


def merge(arr, start, middle, end):
    left = arr[start : middle + 1]
    right = arr[middle + 1 : end + 1]

    k = start
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1


print(merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 8))
