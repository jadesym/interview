class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return " ".join([self.createGoatString(s, vowels, index + 1) for index, s in enumerate(S.split())])
    def createGoatString(self, s, vowels, index):
        first_char = s[0]
        if first_char.lower() in vowels:
            return s + "ma" + "a" * index
        else:
            return s[1:] + s[:1] + "ma" + "a" * index
        
        