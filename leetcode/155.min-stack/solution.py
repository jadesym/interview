class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.min) == 0:
            self.min.append(x)
        elif x < self.min[len(self.min) - 1]:
            self.min.append(x)
        else:
            self.min.append(self.min[len(self.min) - 1])


    def pop(self):
        """
        :rtype: void
        """
        if len(self.min) == 0: return None
        self.min.pop()
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.min) == 0: return None
        return self.stack[len(self.stack) - 1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min) == 0: return None
        return self.min[len(self.min) - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()