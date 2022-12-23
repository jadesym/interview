import math

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        letter_count = 0
        for char in s:
            if char == letter: letter_count += 1
        return math.floor(letter_count / len(s) * 100)