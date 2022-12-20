class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        numBits = 0
        while xor > 0:
            if xor % 2 == 1:
                numBits += 1
                xor -= 1
            else:
                xor //= 2
        return numBits
    