class Solution:
    def repeatedCharacter(self, s: str) -> str:
        char_set = set()
        for char in s:
            if char not in char_set:
                char_set.add(char)
            else:
                return char