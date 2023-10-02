def sortColors(nums):
    count = [0, 0, 0]

    for num in nums:
        count[num] = count[num] + 1

    i = 0

    for idx, num in enumerate(count):
        for _ in range(num):
            nums[i] = idx
            i += 1


arr1 = [2, 0, 2, 1, 1, 0]
sortColors(arr1)
print(arr1)

arr2 = [2, 0, 1]
sortColors(arr2)
print(arr2)

arr3 = [2, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0]
sortColors(arr3)
print(arr3)
