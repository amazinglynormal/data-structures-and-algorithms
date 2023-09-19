import math


# 1 <= k <= max(piles)
def minEatingSpeed(piles, h) -> int:
    k = max(piles)

    l = 1
    r = k

    while l <= r:
        mid = (l + r) // 2
        hours = 0

        for i in piles:
            hours += math.ceil(i / mid)

            if hours > h:
                l = mid + 1
                break

        if hours <= h:
            k = mid
            r = mid - 1

    return k


print(minEatingSpeed([3, 6, 7, 11], 8))  # 4
print(minEatingSpeed([30, 11, 23, 4, 20], 5))  # 30
print(minEatingSpeed([30, 11, 23, 4, 20], 6))  # 23
