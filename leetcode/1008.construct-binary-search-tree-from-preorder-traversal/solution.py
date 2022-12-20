# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            self.insert(root, preorder[i])
        return root
    
    def insert(self, node: TreeNode, val: int):
        if node.val < val:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self.insert(node.right, val)
        else:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self.insert(node.left, val)
            
        