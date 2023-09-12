def choose_pivot_index(arr, start, end):
    middle = (start + end) // 2

    # sort the three values and return middle index

    if arr[start] > arr[end]:
        arr[start], arr[end] = arr[end], arr[start]

    if arr[start] > arr[middle]:
        arr[start], arr[middle] = arr[middle], arr[start]

    if arr[middle] > arr[end]:
        arr[middle], arr[end] = arr[end], arr[middle]

    return middle


def quick_sort(arr, start, end):
    if end - start + 1 <= 1:
        return arr

    pivot_index = choose_pivot_index(arr, start, end)

    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    pointer = start

    for i in range(start, end):
        if arr[i] < arr[end]:
            arr[i], arr[pointer] = arr[pointer], arr[i]
            pointer += 1

    arr[pointer], arr[end] = arr[end], arr[pointer]

    quick_sort(arr, start, pointer - 1)
    quick_sort(arr, pointer + 1, end)

    return arr


print(quick_sort([9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 8))
print(quick_sort([6, 8, 3, 6, 9, 4, 15, 2, 5], 0, 8))
print(quick_sort([9, 11, 36, 6, 5, -8, 27, 2, 1], 0, 8))
