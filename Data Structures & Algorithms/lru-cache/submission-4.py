class Node:
    def __init__(self, key=None,val=None):
        self.val = val
        self.prev = None
        self.next = None
        self.key = key
class LRUCache:


    def __init__(self, capacity: int):
        #doubly linked list for O(1) insert and delete
        #hashmap: Node for O(1) get
        self.capacity = capacity
        self.hm = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def removeNode(self,key):
        # removes node from linked list, and deletes entry from hashmap
        n = self.hm[key]
        prev,after = n.prev, n.next
        prev.next = after
        after.prev = prev
        n.prev =None
        n.next = None
        del self.hm[key]
        return n

    def insertNode(self, key, n):
        # checks capacity, if exceed capacity it will remove least recently used key
        if len(self.hm) == self.capacity:
            k = self.tail.prev.key
            self.removeNode(k)
        # inserts node as most recently used (self.head.next)
        currMRU = self.head.next
        self.head.next = n
        n.prev = self.head
        n.next = currMRU
        currMRU.prev = n
        self.hm[key] = n
           

    def get(self, key: int) -> int:
        # check if key exists in hm, if exists need to update the node to become
        #most recently used
        #if not inside directly return
        if key not in self.hm:return -1
        n = self.removeNode(key)
        self.insertNode(key, n)
        return n.val

    def put(self, key: int, value: int) -> None:
        # if put duplicate key need remove
        if key in self.hm:
            self.removeNode(key)
        n = Node(key,value)
        self.insertNode(key, n)
        
