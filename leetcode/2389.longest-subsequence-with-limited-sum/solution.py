class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        sums = [None] * len(nums)
        sum_so_far = 0
        for i in range(len(nums)):
            sum_so_far += sorted_nums[i]
            sums[i] = sum_so_far
        # print(sums)
        result = []
        for query in queries:
            max_nums = self.find(sums, 0, len(sums) - 1, query) + 1
            result.append(max_nums)
            # print(query, max_nums)
        return result
    def find(self, sums: List[int], low: int, high: int, val: int) -> int:
        if low == high:
            if sums[low] > val:
                return low - 1
            return low
        elif low == high - 1:
            if sums[low] > val:
                return low -1
            elif sums[high] > val:
                return low
            else:
                return high
        mid = (low + high) // 2

        mid_val = sums[mid]
        if mid_val > val:
            return self.find(sums, low, mid - 1, val)
        else:
            return self.find(sums, mid, high, val)