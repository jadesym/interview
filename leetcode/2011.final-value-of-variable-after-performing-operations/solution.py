class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        val = 0
        for op in operations:
            if op[1] == "-":
                val -= 1
            else:
                val += 1
                
        return val
        