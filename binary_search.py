def binary_search(nums, target) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return -1


print(binary_search([-1, 0, 3, 5, 9, 12], 9))
print(binary_search([-1, 0, 3, 5, 9, 12], 2))
print(binary_search([5], 5))
