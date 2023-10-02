class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

        def __str__(self):
            return f"val = {self.val}, next = {self.next}"

    def get(self, index: int) -> int:
        if self.length == 0:
            return -1

        curr_node = self.head
        for i in range(index + 1):
            if curr_node.next is None and i != index:
                return -1
            elif i == index:
                return curr_node.val
            else:
                curr_node = curr_node.next

    def addAtHead(self, val: int) -> None:
        old_head = self.head
        new_head = self.Node(val, old_head)
        self.head = new_head
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            return self.addAtHead(val)

        curr_head = self.head

        while not (curr_head.next is None):
            curr_head = curr_head.next

        new_tail = self.Node(val)
        curr_head.next = new_tail

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return

        if index == 0:
            return self.addAtHead(val)

        if index == self.length:
            return self.addAtTail(val)

        curr_node = self.head
        new_node = self.Node(val)

        for i in range(index - 1):
            curr_node = curr_node.next

        new_node.next = curr_node.next
        curr_node.next = new_node

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return

        curr_head = self.head

        if index == 0:
            new_head = curr_head.next
            self.head = new_head
            self.length -= 1
            return

        for i in range(index - 1):
            curr_head = curr_head.next

        curr_head.next = curr_head.next.next
        self.length -= 1
