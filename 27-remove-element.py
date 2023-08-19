# val 0 <= val <= 100
def removeElement(nums, val) -> int:
    k = 0
    i = 0
    j = len(nums) - 1

    while i <= j:
        if nums[i] != val:
            k += 1
            i += 1
            continue

        nums[i] = -1
        nums[i], nums[j] = nums[j], nums[i]
        j -= 1

    return k
