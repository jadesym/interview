class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        num_mapping = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in num_mapping:
                num_mapping[num] = []
            num_mapping[num].append(i)
        
        count = 0

        for num, arr in num_mapping.items():
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    if (arr[i] * arr[j]) % k == 0:
                        count += 1
        return count