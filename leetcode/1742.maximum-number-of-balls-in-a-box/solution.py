class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ballCounts = {}
        maxBalls = None
        for i in range(lowLimit, highLimit + 1):
            digitSum = self.getDigitSum(i)
            if digitSum not in ballCounts: ballCounts[digitSum] = 0
            ballCounts[digitSum] += 1
            if maxBalls is None:
                maxBalls = ballCounts[digitSum]
            else:
                maxBalls = max(ballCounts[digitSum], maxBalls)
        return maxBalls
        
    def getDigitSum(self, val: int) -> int:
        digitSum = 0
        curVal = val

        while curVal > 0:
            digit = curVal % 10
            digitSum += digit
            curVal //= 10
        return digitSum