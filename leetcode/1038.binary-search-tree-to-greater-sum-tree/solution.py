# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstTraverse(self, curNode: TreeNode, vals: list):
        if curNode is None: return
        self.bstTraverse(curNode.right, vals)
        vals.append(curNode.val)
        self.bstTraverse(curNode.left, vals)

    def gstReplace(self, curNode: TreeNode, valsToSum: dict):
        if curNode is None: return
        self.gstReplace(curNode.right, valsToSum)
        curNode.val = valsToSum[curNode.val]
        self.gstReplace(curNode.left, valsToSum)
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        vals = []
        self.bstTraverse(root, vals)

        valsToSum = {}
        curSum = 0
        for val in vals:
            valsToSum[val] = val + curSum
            curSum = valsToSum[val]

        self.gstReplace(root, valsToSum)
        return root