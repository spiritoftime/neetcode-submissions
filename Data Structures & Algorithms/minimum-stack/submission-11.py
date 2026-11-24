class MinStack:
    # normal stack is able to run top(), pop(), push() in O(1) time.
    # getMin is the issue
    # at every index, we should mainitain a reference to the minimum.

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack: # first element to be added
            # first element is value of element here, 2nd is minimum
            self.stack.append([val,val]) 
        else:
            self.stack.append([val,min(self.stack[-1][1], val)])
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
    def top(self) -> int:
        return self.stack[-1][0] # stack is FILO
        
    def getMin(self) -> int:
        return self.stack[-1][-1]
        
