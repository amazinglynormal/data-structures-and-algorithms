class MyHashMap:
    def __init__(self):
        self.buckets = [Bucket()] * 10007

    def hash_key(self, key):
        return key % 10007

    def put(self, key: int, value: int) -> None:
        hashed_key = self.hash_key(key)
        self.buckets[hashed_key].insert(key, value)

    def get(self, key: int) -> int:
        hashed_key = self.hash_key(key)
        return self.buckets[hashed_key].get_value(key)

    def remove(self, key: int) -> None:
        hashed_key = self.hash_key(key)
        self.buckets[hashed_key].delete(key)


class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class Bucket:
    def __init__(self):
        self.head = Node(0, 0)

    def insert(self, key, value):
        if not self.key_exists(key):
            new_node = Node(key, value, self.head.next)
            self.head.next = new_node
        elif self.get_value(key) != value:
            self.change_value_of_key(key, value)

    def key_exists(self, key):
        curr = self.head.next
        while curr is not None:
            if curr.key == key:
                return True
            curr = curr.next

    def get_value(self, key):
        curr = self.head.next
        while curr is not None:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1

    def delete(self, key):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.key == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def change_value_of_key(self, key, new_value):
        curr = self.head.next
        while curr.key != key:
            curr = curr.next
        curr.value = new_value
