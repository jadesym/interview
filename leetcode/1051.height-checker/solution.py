class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        count = 0
        for i in range(len(sorted_heights)):
            if sorted_heights[i] != heights[i]: count += 1
        return count