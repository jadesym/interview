class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedChars = set([char for char in allowed])

        goodWords = 0
        for word in words:
            isWordBad = False
            
            for char in word:
                
                if char not in allowedChars:
                    isWordBad = True
                    break
            if not isWordBad:
                goodWords += 1
        return goodWords