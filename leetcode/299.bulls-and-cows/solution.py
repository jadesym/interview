class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        correct = 0
        wrongPosition = 0
        correctNums = [0]*10
        secretNums = [0]*10
        guessNums = [0]*10
        for index in range(len(secret)):
            secretChar = secret[index]
            guessChar = guess[index]
            if secretChar == guessChar:
                correct += 1
                correctNums[int(secretChar)] += 1
            else:
                secretNums[int(secretChar)] += 1
                guessNums[int(guessChar)] += 1
        for index in range(10):
            wrongPosition += min(guessNums[index], secretNums[index])
        result = str(correct) + "A" + str(wrongPosition) + "B"
        return result
        