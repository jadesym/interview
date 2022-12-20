class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        
        currentLongest = ""
        index = 0
        char = None
        error = False
        while not error:
            for string in strs:
                if len(string) == 0 or index >= len(string):
                    error = True
                    char = None
                    break
                elif char is None:
                    char = string[index]
                else:
                    if string[index] != char: 
                        error = True
                        char = None
                        break
            if char is not None:
                currentLongest += char
                char = None
                index += 1
            else:
                break
        return currentLongest
            