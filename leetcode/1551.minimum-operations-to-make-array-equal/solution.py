class Solution:
    def minOperations(self, n: int) -> int:
        half_of_elems_to_change = n // 2
        if n % 2 == 1:
            return half_of_elems_to_change * (half_of_elems_to_change + 1)
        else:
            return half_of_elems_to_change ** 2