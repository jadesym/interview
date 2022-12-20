class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        for num in nums:
            if num < 0: negatives.append(num)
            else: positives.append(num)
        result = []
        for i in range(len(positives)):
            result.append(positives[i])
            result.append(negatives[i])
        return result