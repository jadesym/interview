class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        num_set = set(nums)
        distincts = set()
        for num in num_set:
            distincts.add(num)
            digits = self.getDigits(num)
            reverseDigits = self.reverseDigits(digits)
            reversedNum = self.constructNum(reverseDigits)
            distincts.add(reversedNum)
            # print(num, reversedNum)

        # print(distincts)
        return len(distincts)

    def reverseDigits(self, digits: List[int]) -> List[int]:
        return list(reversed(digits))

    def constructNum(self, digits: List[int]):
        if len(digits) == 1: return digits[0]
        num = 0
        for i in range(len(digits) - 1, 0, -1):
            digit = digits[i]
            num += digit
            num *= 10
        num += digits[0]
        return num

    def getDigits(self, num: int) -> List[int]:
        digits = []
        curNum = num
        while curNum > 0:
            digits.append(curNum % 10)
            curNum //= 10
        return digits