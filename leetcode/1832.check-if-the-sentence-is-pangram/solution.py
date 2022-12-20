class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        char_set= set()
        for char in sentence:
            if char not in char_set:
                char_set.add(char)
        
        return len(char_set) >= 26
    
        
        