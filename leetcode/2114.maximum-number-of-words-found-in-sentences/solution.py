class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        maximum = 0
        for sentence in sentences:
            currentSpaces = 0
            for char in sentence:
                if char == " ":
                    currentSpaces += 1
            currentWords = currentSpaces + 1
            if currentWords > maximum:
                maximum = currentWords
        return maximum