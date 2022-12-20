class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evens = 0
        for num in nums:
            if self.getNumDigits(num) % 2 == 0:
                evens += 1
        return evens
    def getNumDigits(self, num: int) -> int:
        digits = 0
        curNum = num
        while curNum > 0:
            curNum //= 10
            digits += 1
        return digits