# Alternate solution would be to use a stack, which would also
# imply that recursion can be used

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"val => {self.val}, next => {self.next}"


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # reverse list while traversing to last node

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        curr = prev
        prev = None

        carried = 0

        while curr:
            # double val and account carry 1 if neccessary
            new_val = curr.val * 2 + carried
            if new_val >= 10:
                carried = 1
                new_val -= 10
            else:
                carried = 0
            curr.val = new_val

            # un-reverse list
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        if carried == 1:
            return ListNode(1, prev)
        else:
            return prev


sol = Solution()

l1 = ListNode(1)
l2 = ListNode(8)
l3 = ListNode(9)

l1.next = l2
l2.next = l3

print(sol.doubleIt(l1))

l4 = ListNode(9)
l5 = ListNode(9)
l6 = ListNode(9)

l4.next = l5
l5.next = l6

print(sol.doubleIt(l4))

l7 = ListNode(5)
print(sol.doubleIt(l7))
