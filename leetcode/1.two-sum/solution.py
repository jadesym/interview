class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_map = {}
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            if diff in num_index_map:
                return [num_index_map[diff], i]

            if num not in num_index_map:
                num_index_map[num] = i
        return None