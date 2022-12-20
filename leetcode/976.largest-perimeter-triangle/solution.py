class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sorted_a = sorted(A)
        low_index = len(sorted_a) - 3
        mid_index = len(sorted_a) - 2
        high_index = len(sorted_a) - 1
        while low_index > -1:
            low = sorted_a[low_index]
            mid = sorted_a[mid_index]
            high = sorted_a[high_index]
            if self.isTriangle(low, mid, high):
                return low + mid + high
            if mid_index - low_index > 1: mid_index -= 1
            if high_index - mid_index > 1: high_index -= 1
            else: low_index -= 1
        return 0
    def isTriangle(self, low, mid, high):
        return (low + mid) > high
        