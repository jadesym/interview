class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than_nums = []
        greater_than_nums = []
        equal_nums = []
        for num in nums:
            if num < pivot:
                less_than_nums.append(num)
            elif num > pivot:
                greater_than_nums.append(num)
            else:
                equal_nums.append(num)
        return less_than_nums + equal_nums + greater_than_nums