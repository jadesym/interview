class NumArray(object):
    def __init__(self, nums):
        self.cache = [0]*len(nums)
        sumSoFar = 0
        for index in range(len(nums)):
            sumSoFar+=nums[index]
            self.cache[index] = sumSoFar
        """
        initialize your data structure here.
        :type nums: List[int]
        """

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0: return self.cache[j]
        return self.cache[j] - self.cache[i - 1]
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)