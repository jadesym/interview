class MyQueue:

    def __init__(self):
        self.firstStack = []
        self.secondStack = []

    # [1, 2] [2, 1]
    def push(self, x: int) -> None:
        self.firstStack.append(x)
        originalSecondStackLen = len(self.secondStack)
        while len(self.secondStack) > 0:
            self.firstStack.append(self.secondStack.pop())
        self.secondStack.append(x)
        for i in range(originalSecondStackLen):
            self.secondStack.append(self.firstStack.pop())


    # Should pop first rather than last
    def pop(self) -> int:
        self.secondStack.pop()
        originalFirstStackLen = len(self.firstStack)
        while len(self.firstStack) > 1:
            self.secondStack.append(self.firstStack.pop())
        val = self.firstStack.pop()
        for i in range(originalFirstStackLen - 1):
            self.firstStack.append(self.secondStack.pop())
        return val
        
    # Should show first rather than last
    def peek(self) -> int:
        return self.secondStack[len(self.secondStack) - 1]

    def empty(self) -> bool:
        return len(self.firstStack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()