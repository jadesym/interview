line1 = 'qwertyuiop'
line2 = 'asdfghjkl'
line3 = 'zxcvbnm'

class Solution(object):
    def __init__(self):
        self.lookup = {}
        for char in line1:
            self.lookup[char] = 1
        for char in line2:
            self.lookup[char] = 2
        for char in line3:
            self.lookup[char] = 3

    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        results = []
        for word in words:
            line = None
            inSameLine = True
            for char in word.lower():
                wordLine = self.lookup[char]
                if line is None:
                    line = wordLine
                elif line != wordLine:
                    inSameLine = False
                    break
            if inSameLine:
                results.append(word)
        return results
            
                