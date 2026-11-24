
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.l, self.r = Node(0, 0), Node(0, 0)
        self.l.next = self.r
        self.r.prev = self.l
        self.cache = {}

    def remove(self, n: Node):
        """removes a node and clears it from the cache"""
        key = n.key
        prev, next = n.prev, n.next
        prev.next = next
        next.prev = prev
        n.next, n.prev = None, None
        del self.cache[key]

    def insert(self, n: Node):
        """inserts the node as most recently used, and adds it to the cache"""
        prev = self.r.prev
        prev.next = n
        n.prev = prev
        n.next = self.r
        self.r.prev = n
        self.cache[n.key] = n

    def get(self, key: int) -> int:
        # if item is inside, need to shift it to the right (most recently used) before returning
        if key in self.cache:
            n = self.cache[key]
            self.remove(n)
            self.insert(n)
            return n.val
        return -1

    def put(self, key: int, value: int) -> None:
        # if exist -> update value of the key, put it on the most recently used
        n = Node(key, value)
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(n)
        else:
            # if doesnt exist, need to pop the lru before adding
            if len(self.cache) + 1 > self.capacity:
                self.remove(self.l.next)  # remove least recently used
                self.insert(n)
            else:  # within capacity constraints, just insert it
                self.insert(n)