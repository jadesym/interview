class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_counts = {}
        for num in arr:
            if num not in num_counts: num_counts[num] = 0
            num_counts[num] += 1
        count_set = set(num_counts.values())
        # print(len(num_counts.keys()), count_set)
        # print(num_counts)
        return len(count_set) == len(num_counts.keys())