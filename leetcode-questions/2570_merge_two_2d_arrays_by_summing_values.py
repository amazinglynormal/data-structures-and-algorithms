from typing import List


def mergeArrays(nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
    result = []
    ptr1 = 0
    ptr2 = 0

    while ptr1 < len(nums1) and ptr2 < len(nums2):
        ptr1_id = nums1[ptr1][0]
        ptr2_id = nums2[ptr2][0]

        if ptr1_id == ptr2_id:
            merge_val = nums1[ptr1][1] + nums2[ptr2][1]
            result.append([ptr1_id, merge_val])
            ptr1 += 1
            ptr2 += 1
            continue

        if ptr1_id < ptr2_id:
            result.append(nums1[ptr1])
            ptr1 += 1
        else:
            result.append(nums2[ptr2])
            ptr2 += 1

    while ptr1 < len(nums1):
        result.append(nums1[ptr1])
        ptr1 += 1

    while ptr2 < len(nums2):
        result.append(nums2[ptr2])
        ptr2 += 1

    return result


print(mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]))
print(mergeArrays([[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]]))
