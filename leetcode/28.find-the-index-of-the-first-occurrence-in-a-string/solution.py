class Solution(object):
    def preprocessNeedle(self, needle):
        needleArray = [0] * len(needle)
        i, j = 0, 1
        while j < len(needle):
            if needle[i] == needle[j]:
                needleArray[j] = i + 1
                i+=1
                j+=1
            elif needle[i] != needle[j] and i == 0:
                needleArray[j] = 0
                j+=1
            else:
                i = needleArray[i- 1]
        return needleArray
        
    
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0: return 0
        needleArray = self.preprocessNeedle(needle)
        a, b = 0, 0
        curIndex = None
        while a < len(haystack) and b < len(needle):
            if haystack[a] == needle[b]:
                if curIndex is None:
                    curIndex = a - b 
                a += 1
                b += 1
            else:
                curIndex = None
                if b != 0: 
                    b = needleArray[b - 1]
                else: a += 1
        return curIndex if b == len(needle) else -1