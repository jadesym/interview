# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.getAverageAndNodeAverageCount(root)[2]
    def getAverageAndNodeAverageCount(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return (0, 0, 0)
        (leftTotal, leftAverageNodeCount, leftTotalNestedAverageNodes) = self.getAverageAndNodeAverageCount(node.left)
        (rightTotal, rightAverageNodeCount, rightTotalNestedAverageNodes) = self.getAverageAndNodeAverageCount(node.right)
        curNodeValue = node.val
        # print(curNodeValue, leftTotal, leftAverageNodeCount, leftTotalNestedAverageNodes, rightTotal, rightAverageNodeCount, rightTotalNestedAverageNodes)

        if leftAverageNodeCount + rightAverageNodeCount == 0:
            return (curNodeValue, 1, 1)

        curNodeTotal = (leftTotal + rightTotal + curNodeValue)
        roundedAverage =  (leftTotal + rightTotal + curNodeValue) // (leftAverageNodeCount + rightAverageNodeCount + 1)
        doesValMatchAverage = roundedAverage == curNodeValue

        return (curNodeTotal, (leftAverageNodeCount + rightAverageNodeCount + 1), (1 if doesValMatchAverage else 0) + leftTotalNestedAverageNodes + rightTotalNestedAverageNodes)

        
        
        
        