class Node:
    def __init__(self, key=None,val=None):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {}
        self.head = Node()
        self.tail = Node()
        self.capacity = capacity

        self.head.next = self.tail
        self.tail.prev = self.head

    def removeNode(self, key) -> Node:
        before = self.hm[key].prev
        after = self.hm[key].next
        before.next = after
        after.prev = before
        n = self.hm[key]
        # remove from hm
        del self.hm[key]
        return n
    # inserts a node as the most recently used
    def insertNode(self, key,val) -> Node:
        n = Node(key,val)
        # put node in hm
        self.hm[key] = n
        # if already reach capacity, evict least recently used
        if len(self.hm.keys()) > self.capacity:
            self.removeNode(self.tail.key)
        #if not reach capacity, can insert the node to the list, and put in the cache
        currHead = self.head.next
        mru = self.head.next
        mru.prev = n
        self.head.next = n
        n.prev = self.head
        n.next = mru
        return n
    def get(self, key: int) -> int:
        # if it doesnt exist, return -1
        if key not in self.hm: return -1
        # if it does exist, need to put it as the most recently used, which is right before head
        n = self.removeNode(key)
        self.insertNode(key,n.val)
        return self.hm[key].val

    def put(self, key: int, value: int) -> None:


        # if key exists, update value, put as mru.
        if key in self.hm:
            self.removeNode(key)
        # if key dont exist, put as mru
        else:
            if len(self.hm.keys()) == self.capacity:
                self.removeNode(self.tail.prev.key)
        n = self.insertNode(key,value)
        self.hm[key] = n

        
