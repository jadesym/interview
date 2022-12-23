class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        elif len(nums) == 1: return [[nums[0]]]
        perms = []
        for i in range(len(nums)):
            item = nums[i]
            remaining = nums[:i] + nums[i+1:]
            nested_perms = self.permute(remaining)
            for nested_perm in nested_perms:
                perms.append([item] + nested_perm)
        return perms