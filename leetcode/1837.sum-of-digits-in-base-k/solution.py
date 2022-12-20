class Solution:
    def sumBase(self, n: int, k: int) -> int:
        result = 0
        curNum = n
        while curNum > 0:
            digit = curNum % k
            curNum //= k
            result += digit
        return result