class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        numFirstHalf = 0
        numSecondHalf = 0
        for i in range(len(s) // 2):
            if s[i] in vowels: numFirstHalf += 1
        for j in range(len(s) // 2, len(s)):
            if s[j] in vowels: numSecondHalf += 1
        return numFirstHalf == numSecondHalf
