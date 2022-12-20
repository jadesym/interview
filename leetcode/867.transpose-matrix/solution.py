class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        array = []
        for y in range(len(A[0])):
            nested_array = []
            for x in range(len(A)):
                nested_array.append(A[x][y])
            array.append(nested_array)
        return array