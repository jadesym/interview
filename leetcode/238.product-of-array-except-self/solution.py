class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prev = []
        after = [1]*len(nums)
        prevProduct = 1
        afterProduct = 1
        for x in range(len(nums)):
            num = nums[x]
            prevProduct *= num
            prev.append(prevProduct)
        for y in range(len(nums) - 1, -1, -1):
            num = nums[y]
            afterProduct *= num
            after[y] = afterProduct
        output = []
        for y in range(len(nums)):
            if y == 0:
                output.append(after[y+1])
            elif y == len(nums) - 1:
                output.append(prev[y - 1])
            else:
                output.append(prev[y-1] * after[y+1])
        return output
        