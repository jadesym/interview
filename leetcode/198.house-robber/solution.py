class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxWhenRobbed = [0]*len(nums)
        maxWhenUnrobbed = [0]*len(nums)
        if len(nums) == 0: return 0
        elif len(nums) == 1: return nums[0]
        maxWhenRobbed[0] = nums[0]
        maxWhenRobbed[1] = max(nums[1], maxWhenRobbed[0])
        for index in range(2, len(nums)):
            curHouse = nums[index]
            maxWhenRobbed[index] = max(maxWhenRobbed[index-2] + curHouse, maxWhenUnrobbed[index-1] + curHouse, maxWhenUnrobbed[index-2] + curHouse)
            maxWhenUnrobbed[index] = max(maxWhenRobbed[index-1], maxWhenUnrobbed[index-1])
        return max(maxWhenRobbed[len(nums)-1], maxWhenUnrobbed[len(nums)-1])
            
        