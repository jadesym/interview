class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 1: return False
        num_count = {}
        for num in nums:
            if num not in num_count: num_count[num] = 0
            num_count[num] += 1
        for num, count in num_count.items():
            if count % 2 == 1: return False
        return True