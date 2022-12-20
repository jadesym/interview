class Solution:
    def letterCasePermutation(self, S: 'str') -> 'List[str]':
        results = []
        self.dfsPermutations(S, '', results)
        return results
    def dfsPermutations(self, originalString, stringSoFar, results):
        currentIndex = len(stringSoFar)
        if currentIndex >= len(originalString):
            results.append(stringSoFar)
            return
        currentLetter = originalString[currentIndex]
        if currentLetter.isalpha():
            self.dfsPermutations(originalString, stringSoFar + currentLetter, results)
            self.dfsPermutations(originalString, stringSoFar + (currentLetter.upper() if currentLetter.islower() else currentLetter.lower()), results)
        else:
            self.dfsPermutations(originalString, stringSoFar + currentLetter, results)