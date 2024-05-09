class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __str__(self) -> str:
        return f"val => {self.val}, next => {self.next}"


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        prev = node

        while node.next:
            node.val = node.next.val
            prev = node
            node = node.next

        prev.next = None


l4 = ListNode(9)
l3 = ListNode(1, l4)
l2 = ListNode(5, l3)
l1 = ListNode(4, l2)

sol = Solution()

sol.deleteNode(l2)

print(l1)
