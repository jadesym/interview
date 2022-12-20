class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        result = [0] * len(boxes)
        for i in range(len(result)):
            for j in range(len(boxes)):
                if boxes[j] != "0":
                    result[i] += abs(i  - j)
        return result
                
                
        