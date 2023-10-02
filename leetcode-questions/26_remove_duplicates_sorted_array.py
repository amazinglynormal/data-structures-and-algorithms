def removeDuplicates(nums) -> int:
    if len(nums) == 1:
        return 1

    pointerA = 0
    pointerB = 1

    unique_elements = len(nums)

    while pointerB < len(nums):
        if nums[pointerA] == nums[pointerB]:
            nums[pointerB] = 101
            pointerB += 1
            unique_elements -= 1
            continue
            
        pointerB += 1
        pointerA = pointerB - 1

    nums.sort()

    return unique_elements
