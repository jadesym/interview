class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = []
        curNum = num
        index = 0
        last6Index = None
        while curNum > 0:
            remainder = curNum % 10
            if remainder == 6:
                last6Index = index
            index += 1
            curNum //= 10
        if last6Index is not None:
            return num + 10**last6Index * 3
        else:
            return num