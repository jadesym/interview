# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals = []
        self.get_vals(root, vals)
        sorted_vals = sorted(vals)
            
        newRoot = TreeNode(sorted_vals[len(sorted_vals) // 2])
        left_vals = sorted_vals[0:len(sorted_vals) // 2]
        right_vals = sorted_vals[len(sorted_vals) // 2 + 1:len(sorted_vals)]

        self.insert_nodes(newRoot, left_vals)
        self.insert_nodes(newRoot, right_vals)
        return newRoot

    def get_vals(self, node: TreeNode, valsSoFar: List[int]) -> None:
        if node is None: return
        valsSoFar.append(node.val)
        self.get_vals(node.right, valsSoFar)
        self.get_vals(node.left, valsSoFar)
        return

    def insert_nodes(self, node: TreeNode, valsToInsert: List[int]) -> None:
        if len(valsToInsert) == 0:
            return

        midVal = valsToInsert[len(valsToInsert) // 2]
        left_vals = valsToInsert[0:len(valsToInsert) // 2]
        right_vals = valsToInsert[len(valsToInsert) // 2 + 1:len(valsToInsert)]

        if midVal < node.val:
            node.left = TreeNode(midVal)
            self.insert_nodes(node.left, left_vals)
            self.insert_nodes(node.left, right_vals)
        else:
            node.right = TreeNode(midVal)
            self.insert_nodes(node.right, left_vals)
            self.insert_nodes(node.right, right_vals)


