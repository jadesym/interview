class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if len(nums) == 1: return 1
        sorted_nums = sorted(nums)

        partition_count = 0

        minNum = None
        # print(sorted_nums)

        for i in range(len(sorted_nums)):
            num = sorted_nums[i]
            if minNum is None:
                minNum = num
            elif num > k + minNum:
                # print(minNum, num, i)
                partition_count += 1
                minNum = num
        partition_count += 1
        
        return partition_count
        