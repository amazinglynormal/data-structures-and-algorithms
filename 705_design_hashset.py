class MyHashSet:
    def __init__(self):
        INITIAL_CAPACITY = 1000
        self.buckets = [None] * INITIAL_CAPACITY

    def hash_key(self, key):
        return key % 1000

    def add(self, key: int) -> None:
        hash = self.hash_key(key)
        if self.buckets[hash] is None:
            self.buckets[hash] = key
        else:
            if isinstance(self.buckets[hash], list) and not key in self.buckets[hash]:
                self.buckets[hash].append(key)
            elif isinstance(self.buckets[hash], list) or self.buckets[hash] == key:
                return None
            else:
                value = self.buckets[hash]
                self.buckets[hash] = [value, key]

    def remove(self, key: int) -> None:
        hash = self.hash_key(key)
        if isinstance(self.buckets[hash], list) and key in self.buckets[hash]:
            self.buckets[hash].remove(key)
        elif isinstance(self.buckets[hash], list) and not key in self.buckets[hash]:
            return None
        elif self.buckets[hash] != key:
            return None
        else:
            self.buckets[hash] = None

    def contains(self, key: int) -> bool:
        hash = self.hash_key(key)
        if isinstance(self.buckets[hash], list):
            if key in self.buckets[hash]:
                return True
        elif self.buckets[hash] == key:
            return True
        return False
