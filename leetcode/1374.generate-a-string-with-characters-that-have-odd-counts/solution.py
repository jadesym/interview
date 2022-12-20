class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1: return "a" * n
        if n % 2 == 0: return "a" * (n - 1) + "b"