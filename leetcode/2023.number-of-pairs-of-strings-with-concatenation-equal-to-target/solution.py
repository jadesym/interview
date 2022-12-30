class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        num_counts = {}
        for num in nums:
            if num not in num_counts: num_counts[num] = 0
            num_counts[num] += 1
        pair_count = 0
        for first, second in self.targetPairs(target):
            if first == second and first in num_counts:
                count = num_counts[first]
                if count > 1:
                    pair_count += count * (count - 1)
            else:
                if first not in num_counts: continue
                if second not in num_counts: continue
                pair_count += num_counts[first] * num_counts[second]
        return pair_count

    def targetPairs(self, target: str) -> List[tuple[str, str]]:
        pairs = []
        for i in range(1, len(target)):
            pairs.append((target[:i], target[i:]))
        return pairs