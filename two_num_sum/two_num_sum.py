class TwoNumSumSlowTest:
    # O(1) store and O(n) test
    def __init__(self):
        self.numHash = {}
    def store_multiple(self, vals):
        for val in vals: self.store(val)
    def store(self, val):
        if val in self.numHash: self.numHash[val] += 1
        else: self.numHash[val] = 1
    def test(self, sumVal):
        for val in self.numHash.keys():
            diff = sumVal - val
            if diff == val:
                if self.numHash[diff] > 1: return True
            else:
                if diff in self.numHash: return True
        return False

class TwoNumSumFastTest:
    # O(n) store hand O(1) test
    def __init__(self):
        self.nums = {}
        self.sums = {}
    def store_multiple(self, vals):
        for val in vals: self.store(val)
    def store(self, val):
        for num in self.nums.keys():
            if num + val in self.sums: self.sums[num + val] += 1
            else: self.sums[num+val] = 1
        if val in self.nums: self.nums[val] += 1
        else: self.nums[val] = 1
    def test(self, sumVal):
        if self.sums[sumVal] > 0: return True
        return False
