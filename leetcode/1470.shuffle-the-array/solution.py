class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        newNums = []
        for i in range(len(nums) // 2):
            j = i + len(nums) // 2
            newNums.append(nums[i])
            newNums.append(nums[j])
        return newNums
            
        