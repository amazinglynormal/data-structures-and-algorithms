from typing import Optional


class Node:
    def __init__(self, key: int, val: int, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev: Optional[Node] = prev
        self.next: Optional[Node] = next


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def get_head(self) -> Node:
        return self.head

    def add_to_tail(self, node: Node) -> None:
        if not node:
            return

        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def unlink(self, node: Node) -> None:
        if not node:
            return None

        prev = node.prev
        next = node.next

        if prev:
            prev.next = next

        if next:
            next.prev = prev

        if self.head == node:
            self.head = next
        if self.tail == node:
            self.tail = prev

        node.prev = None
        node.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.LRUList = LinkedList()

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1

        self.LRUList.unlink(node)
        self.LRUList.add_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            if self.size + 1 > self.capacity:
                head = self.LRUList.get_head()
                self.cache.pop(head.key)
                self.LRUList.unlink(head)

            new_node = Node(key, value)
            self.LRUList.add_to_tail(new_node)
            self.cache[key] = new_node
            self.size += 1
        else:
            self.LRUList.unlink(node)
            node.val = value
            self.cache[key] = node
            self.LRUList.add_to_tail(node)


lRUCache = LRUCache(2)
lRUCache.put(1, 1)  # cache is {1=1}
lRUCache.put(2, 2)  # cache is {1=1, 2=2}
print(lRUCache.get(1))  # return 1
lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))  # returns -1 (not found)
lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))  # return -1 (not found)
print(lRUCache.get(3))  # return 3
print(lRUCache.get(4))  # return 4
