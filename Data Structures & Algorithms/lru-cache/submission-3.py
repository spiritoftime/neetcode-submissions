class ListNode:
    def __init__(self, key = None, val = None):
        self.val = val
        self.prev = None
        self.next = None
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        # self.head.next is the most recently used
        # self.tail.prev is the least recently used
        self.capacity = capacity
        self.hm = {}
        self.head = ListNode()
        self.tail = ListNode()
        curr = self.head
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeNode(self, key):
        # removes the node. used for reallocating existing key to recent, or to 
        # get rid of something when there is no capacity
        node = self.hm[key]
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before
        node.next = None
        node.prev = None
        # update the hashmap
        del self.hm[node.key]
        return node

    def insertMRUNode(self, key, val):
        # inserts the most recently used node
        currMostRecent = self.head.next
        n = ListNode(key, val)
        self.head.next = n
        n.prev = self.head
        n.next = currMostRecent
        currMostRecent.prev = n
        # update hashmap
        self.hm[n.key] = n

    def get(self, key: int) -> int:
        # if exists -> remove it, put on head.next. put it on hashmap
        # else return -1
        if key not in self.hm: return -1
        # node exists
        n = self.removeNode(key)
        self.insertMRUNode(key, n.val)
        return self.hm[key].val

    def put(self, key: int, value: int) -> None:
        # if exists -> remove it first
        if key in self.hm:
            self.removeNode(key)
        # remove it if capacity is lacking
        if len(self.hm) >= self.capacity:
            self.removeNode(self.tail.prev.key)
        self.insertMRUNode(key, value)
        
        
