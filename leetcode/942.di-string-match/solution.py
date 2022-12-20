class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        low = 0
        high = len(S)
        arr_out = []
        for s in S:
            if s == "I":
                arr_out.append(low)
                low += 1
            else:
                arr_out.append(high)
                high -= 1
        arr_out.append(low)
        return arr_out
            
        