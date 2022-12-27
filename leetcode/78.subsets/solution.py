class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return [[]]

        firstNum = nums[0]

        subsets = []

        remaining = nums[1:]
        remaining_subsets = self.subsets(remaining)
        for subset in remaining_subsets:
            subsets.append([firstNum] + subset)
            subsets.append(subset)
        return subsets

