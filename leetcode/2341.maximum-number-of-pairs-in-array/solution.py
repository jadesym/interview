class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
        leftovers = 0
        pairs = 0
        for key, count in counts.items():
            pairs += count // 2
            leftovers += count % 2
        return (pairs, leftovers)