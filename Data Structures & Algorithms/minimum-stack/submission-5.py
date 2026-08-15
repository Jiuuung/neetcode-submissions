class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[]
        self.minNum=float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minNum>val:
            self.minNum=val
            self.minStack.append(val)
        else:
            self.minStack.append(self.minNum)


    def pop(self) -> None:
        a= self.minStack.pop()
        if self.minStack:
            if self.minStack[-1]>a:
                self.minNum=self.minStack[-1]
        else:
            self.minNum=float('inf')
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minNum
