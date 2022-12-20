class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        firstIndex = 0
        secondIndex = len(nums) - 1
        valsFound = 0
        while firstIndex <= secondIndex:
            secondNum = nums[secondIndex]
            if secondNum == val:
                secondIndex -= 1
                valsFound += 1
                continue
            firstNum = nums[firstIndex]
            if firstNum == val:
                nums[secondIndex], nums[firstIndex] = firstNum, secondNum
                firstIndex += 1
                secondIndex -= 1
                valsFound += 1
            else:
                firstIndex += 1
        return len(nums) - valsFound
            
        