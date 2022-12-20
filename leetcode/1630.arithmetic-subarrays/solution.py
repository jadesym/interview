class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            sub_nums = nums[l[i]:r[i]+1]
            sorted_nums = sorted(sub_nums)
            expected_diff = sorted_nums[1] - sorted_nums[0]
            bool_result = True
            for i in range(1, len(sorted_nums)):
                if sorted_nums[i] - expected_diff != sorted_nums[i - 1]:
                    bool_result = False
                    break
            result.append(bool_result)

        return result