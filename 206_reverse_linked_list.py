# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    if head is None:
        return None

    node = head

    while node.next is not None:
        new_head = node.next
        node.next = node.next.next
        new_head.next = head
        head = new_head

    return head
