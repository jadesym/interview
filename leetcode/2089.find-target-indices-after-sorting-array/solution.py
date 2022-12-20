class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        indices = []
        for i in range(len(sorted_nums)):
            num = sorted_nums[i]
            if num == target: indices.append(i)
        return indices
