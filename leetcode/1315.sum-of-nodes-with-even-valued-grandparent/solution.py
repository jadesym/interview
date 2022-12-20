# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparentNested(self, curNode: TreeNode, curParent: TreeNode, curGrandparent: TreeNode) -> int:
        if curNode is None:
            return 0
        curNodeVal = 0
        if curGrandparent is not None and curGrandparent.val % 2 == 0:
            curNodeVal += curNode.val
        leftNodeVal = self.sumEvenGrandparentNested(curNode.left, curNode, curParent)
        rightNodeVal = self.sumEvenGrandparentNested(curNode.right, curNode, curParent)
        return curNodeVal + leftNodeVal + rightNodeVal
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.sumEvenGrandparentNested(root, None, None)
        