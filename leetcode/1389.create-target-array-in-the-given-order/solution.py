class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            num, j = nums[i], index[i]
            target.insert(j, num)
        return target
            
        