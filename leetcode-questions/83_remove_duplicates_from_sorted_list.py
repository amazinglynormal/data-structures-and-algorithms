from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        node = head
        next = head.next

        while next:
            if node.val == next.val:
                next = next.next
                node.next = next
            else:
                next = next.next
                node = node.next

        return head
