class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_counts = {}
        arr_counts = {}
        for num in target:
            if num not in target_counts: target_counts[num] = 0
            target_counts[num] += 1
        for num in arr:
            if num not in arr_counts: arr_counts[num] = 0
            arr_counts[num] += 1

        if len(target_counts) != len(arr_counts): return False

        for num, count in target_counts.items():
            if num not in arr_counts:
                return False
            if target_counts[num] != arr_counts[num]:
                return False
        return True