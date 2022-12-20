from typing import Set

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # max_3_nums = {}
        # for num in nums:
        #     if num not in max_3_nums:
        #         max_3_nums[num] = 0
        #     if max_3_nums[num] < 3:
        #         max_3_nums[num] += 1
        max_3_nums = []
        max_3_map = {}
        for num in nums:
            if num not in max_3_map:
                max_3_map[num] = 0
            max_3_map[num] += 1
            if max_3_map[num] <= 3:
                max_3_nums.append(num)
        sorted_nums = sorted(max_3_nums)
        sorted_num_indices_map = {}
        for x in range(len(sorted_nums)):
            num = sorted_nums[x]
            if num not in sorted_num_indices_map:
                sorted_num_indices_map[num] = set()
            sorted_num_indices_map[num].add(x)

        resultSets = set()
        for i in range(len(sorted_nums)):
            for j in range(i + 1, len(sorted_nums)):
                twoSum = sorted_nums[i] + sorted_nums[j]
                if -twoSum not in sorted_num_indices_map:
                    continue
                matching_indices_set = sorted_num_indices_map[-twoSum]
                for index in matching_indices_set:
                    if index != i and index != j and index > i and index > j:
                        resultSets.add((sorted_nums[i], sorted_nums[j], sorted_nums[index]))
                        break
        return [list(result) for result in resultSets]
                
