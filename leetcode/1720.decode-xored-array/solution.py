class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        current = first
        result = [first]
        for encode in encoded:
            nextVal = current ^ encode
            result.append(nextVal)
            current = nextVal
        return result
            
