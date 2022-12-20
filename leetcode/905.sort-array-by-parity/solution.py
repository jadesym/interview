class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        newA = [0] * len(A)
        even_index = 0
        odd_index = len(A) - 1
        for a in A:
            if a % 2 == 0:
                newA[even_index] = a
                even_index += 1
            else:
                newA[odd_index] = a
                odd_index -= 1
        return newA
                
        