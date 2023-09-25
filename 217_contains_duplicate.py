def containsDuplicate(nums):
    found = set()

    for num in nums:
        if num in found:
            return True
        found.add(num)

    return False
