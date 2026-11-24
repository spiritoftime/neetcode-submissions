class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.min = min(val, self.min)
        self.stack.append([val,self.min])
    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.min = self.stack[-1][1]
        else:
            self.min = float('inf')
    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return null
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return null
        
