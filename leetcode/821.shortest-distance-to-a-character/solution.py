class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        indices = []
        for i in range(len(S)):
            if S[i] == C:
                indices.append(i)

        result = []

        indices_index = 0
        s_index = 0

        while s_index < len(S):
            curIndex = indices[indices_index]

            if indices_index + 1 >= len(indices):
                result.append(abs(s_index - curIndex))
                s_index += 1
                continue

            nextIndex = indices[indices_index + 1]

            if nextIndex <= s_index:
                indices_index += 1
                continue

            result.append(min(abs(s_index - curIndex), abs(nextIndex - s_index)))
            s_index += 1

        return result
            
            
        