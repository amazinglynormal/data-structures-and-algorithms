def isBadVersion(version: int) -> bool:
    if version >= 13:
        return True
    return False


def firstBadVersion(n: int) -> int:
    low = 1
    high = n

    curr = n

    while low <= high:
        ver = (low + high) // 2

        if not isBadVersion(ver):
            low = ver + 1
        elif isBadVersion(ver):
            curr = ver
            high = ver - 1

    return curr


print(firstBadVersion(24))  # 13
