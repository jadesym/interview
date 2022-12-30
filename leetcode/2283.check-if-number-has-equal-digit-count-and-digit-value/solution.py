
class Solution:
    def digitCount(self, num: str) -> bool:
        expected_digits = {}
        actual_digits = {}
        for i in range(len(num)):
            curNum = int(num[i])
            expected_digits[i] = curNum
            
            if curNum not in actual_digits:
                actual_digits[curNum] = 0
            actual_digits[curNum] += 1

        # print(expected_digits, actual_digits)
        digits_set = set(expected_digits.keys()).union(set(actual_digits.keys()))

        for digit in digits_set:
            expected_count = 0 if digit not in expected_digits else expected_digits[digit]
            actual_count = 0 if digit not in actual_digits else actual_digits[digit]
            if expected_count != actual_count: return False

        return True
