class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for pattern in patterns:
            if self.checkPattern(pattern, word): count += 1
        return count
                
    def checkPattern(self, pattern, word:str) -> bool:
        found = False
        for i in range(len(word)):
            char_mismatch = False
            if i + len(pattern) > len(word):
                found = False
                break
            for j in range(len(pattern)):
                if pattern[j] != word[i + j]:
                    char_mismatch = True
                    break
            if not char_mismatch:
                found = True
                break
                
        return found