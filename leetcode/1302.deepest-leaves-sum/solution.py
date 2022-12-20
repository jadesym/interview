# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSumNested(self, curNode: TreeNode, curLevel: int, sumsPerLevel: dict) -> int:
        if curNode is None: return
        if curNode.left is None and curNode.right is None:
            if curLevel in sumsPerLevel:
                sumsPerLevel[curLevel] += curNode.val
            else:
                sumsPerLevel[curLevel] = curNode.val
            return
        self.deepestLeavesSumNested(curNode.left, curLevel + 1, sumsPerLevel)
        self.deepestLeavesSumNested(curNode.right, curLevel + 1, sumsPerLevel)
        return
        
    def deepestLeavesSum(self, root: TreeNode) -> int:
        curLevel = 0
        sumsAtLevel = {}

        self.deepestLeavesSumNested(root, 0, sumsAtLevel)

        maxLevel = max(sumsAtLevel)
        return sumsAtLevel[maxLevel]