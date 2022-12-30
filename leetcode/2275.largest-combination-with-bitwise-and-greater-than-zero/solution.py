from collections import deque

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        candidate_digits = {}
        max_digits = 0

        for candidate in candidates:
            bitDigits = self.getBits(candidate)
            if candidate not in candidate_digits: candidate_digits[candidate] = []
            candidate_digits[candidate].append(bitDigits)
            max_digits = max(max_digits, len(bitDigits))

        totalDigitCounts = [0] * max_digits
        for candidate, digits_list in candidate_digits.items():
            for digits in digits_list:
                # print(candidate, digits)
                for i in range(len(digits)):
                    totalDigitCounts[i] += digits[i]

        return max(totalDigitCounts)

    # lower digits on left
    def getBits(self, num: int) -> List[int]:
        digits = []
        curNum = num
        while curNum > 0:
            digits.append(curNum % 2)
            curNum //= 2
        return digits