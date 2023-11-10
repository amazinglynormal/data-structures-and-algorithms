from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = None
        slow = head
        fast = head.next

        while fast and fast.next:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
            fast = fast.next.next

        start = slow.next
        slow.next = prev

        twinSum = 0
        while slow:
            twinSum = max(twinSum, slow.val + start.val)
            slow = slow.next
            start = start.next

        return twinSum
