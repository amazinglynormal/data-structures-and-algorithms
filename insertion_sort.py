def insertion_sort(arr) -> None:
    for i in range(0, len(arr) - 1):
        j = i
        while j >= 0 and arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1


array = [9, 8, 7, 6, 5, 4, 3, 2, 1]

insertion_sort(array)

print(array)  # [1,2,3,4,5,6,7,8,9]
