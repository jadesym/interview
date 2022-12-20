class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(words) != len(pattern): return False
        dictionary = {}
        reverse = {}
        for index in range(len(pattern)):
            char = pattern[index]
            word = words[index]
            if char in dictionary:
                if dictionary[char] != word: return False
            if word in reverse:
                if reverse[word] != char: return False
            else:
                dictionary[char] = word
                reverse[word] = char
        return True
            