import math

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        a_factors = self.getFactors(a)
        count = 0

        for factor in a_factors:
            if b % factor == 0: count += 1

        if a == b:
            return count + 1
        return count
    def getFactors(self, num: int) -> List[int]:
        result = []

        for i in range(1, num // 2 + 1):
            if num % i == 0: result.append(i)

        return result
        