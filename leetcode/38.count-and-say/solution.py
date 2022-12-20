class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        start = str(1)
        if n == 1: return start
        for x in range(n-1):
            cur = start
            next = ""
            last = None
            count = 0
            for char in cur:
                if last is None: 
                    last = char
                    count += 1
                elif last == char: count += 1
                else: 
                    next += str(count) + str(last) 
                    last = char
                    count = 1
            next += str(count) + str(last)
            start = next    
        return start
        
        