class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            i = 0
            j = len(word) - 1
            not_match = False
            while i < j:
                if word[i] != word[j]:
                    not_match = True
                    break
                i += 1
                j-= 1
            if not not_match:
                return word
            
                
        return ""
        