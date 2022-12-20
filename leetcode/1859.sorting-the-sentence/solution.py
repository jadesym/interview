class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        resultArray = [""] * len(words)
        for word in words:
            wordChars = ""
            indexChars = ""
            for char in word:
                if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
                    wordChars += char
                else:
                    indexChars += char
            index = int(indexChars)
            resultArray[index - 1] = wordChars
        return " ".join(resultArray)