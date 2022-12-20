mappings = {
    'G': 'G',
    '()': 'o',
    '(al)': 'al'
}

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        result = []
        
        currentWord = ""
        for letter in command:
            currentWord += letter

            if currentWord in mappings:
                result.append(mappings[currentWord])
                currentWord = ""
        return "".join(result)