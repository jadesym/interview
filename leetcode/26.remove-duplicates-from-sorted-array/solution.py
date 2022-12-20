class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        lastNum = None
        uniques = 0
        for index in range(len(nums)):
            cur = nums[index]
            if lastNum is None:
                lastNum = cur
                uniques += 1
            elif cur != lastNum:
                nums[uniques] = cur
                uniques += 1
                lastNum = cur
        return uniques
                
                
        
                
                                
                
