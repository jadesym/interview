class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        maxNode = None
        maxCount = 0
        nodeCount = dict()
        for (u, v) in edges:
           
            if u not in nodeCount: nodeCount[u] = 0
            if v not in nodeCount: nodeCount[v] = 0
            nodeCount[u] += 1
            nodeCount[v] += 1

            uCount = nodeCount[u]
            vCount = nodeCount[v]

            
            if maxNode is None:
                if uCount > vCount:
                    maxNode = u
                    maxCount = uCount
                else:
                    maxNode = v
                    maxCount = vCount
            else:
                if uCount > vCount:
                    if uCount > maxCount:
                        maxNode = u
                        maxCount = uCount
                else:
                    if vCount > maxCount:
                        maxNode = v
                        maxCount = vCount
                
        return maxNode
        