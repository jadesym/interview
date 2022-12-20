class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ops = 0
        curNum1, curNum2 = num1, num2
        while curNum1 != 0 and curNum2 != 0:
            opsToAdd, curNum1, curNum2 = self.process(curNum1, curNum2)
            # print(curNum1, curNum2)
            ops += opsToAdd
        return ops
    # opsToAdd, newCurNum1, newCurNum2
    def process(self, num1: int, num2: int) -> tuple[int, int, int]:
        if num1 == 0 or num2 == 0: return (0, num1, num2)
        elif num1 == num2: return (1, 0, num2)
        elif num1 < num2:
            return (num2 // num1, num1, num2 % num1)
        else:
            return (num1 // num2, num1 % num2, num2)