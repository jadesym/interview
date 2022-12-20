from typing import Set

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        lowest = min(nums)
        highest = max(nums)

        smallestDivisorSet = self.getDivisorSet(lowest)
        for i in range(len(smallestDivisorSet) - 1, -1, -1):
            divisor = smallestDivisorSet[i]
            if highest % divisor == 0: return divisor
            
        
    def getDivisorSet(self, num: int) -> List[int]:
        divisors = [1]
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                divisors.append(i)
        divisors.append(num)
        return divisors