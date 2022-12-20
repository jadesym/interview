class RecentCounter:

    def __init__(self):
        self.array = []
        self.low_index = None

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.array.append(t)
        if self.low_index is None:
            self.low_index = 0
        else:
            while self.array[self.low_index] < (t - 3000):
                self.low_index += 1
        return len(self.array) - self.low_index
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)