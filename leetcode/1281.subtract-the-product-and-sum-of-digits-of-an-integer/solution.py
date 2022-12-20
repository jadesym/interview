class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        reversedDigits = []
        curN = n
        while curN > 0:
            reversedDigits.append(curN % 10)
            curN //= 10

        product = 1
        for digit in reversedDigits:
            product *= digit
        return product - sum(reversedDigits)