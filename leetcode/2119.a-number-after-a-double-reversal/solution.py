class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num % 10 != 0 or num == 0