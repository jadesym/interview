class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return
        frontIndex = 0
        backIndex = 0
        while backIndex < len(nums) and frontIndex < len(nums):
            front = nums[frontIndex]
            back = nums[backIndex]
            if frontIndex == backIndex: backIndex += 1
            elif front == 0 and back == 0: backIndex += 1
            elif front == 0:
                nums[backIndex] = front
                nums[frontIndex] = back
                backIndex += 1
                frontIndex += 1
            else:
                frontIndex += 1
        