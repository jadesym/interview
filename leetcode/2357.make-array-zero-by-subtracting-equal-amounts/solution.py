class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        num_set = set(nums)
        sorted_nums = sorted(list(num_set))
        return sum([1 for num in sorted_nums if num > 0])
