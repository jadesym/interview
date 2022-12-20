# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [(root, 0)]

        # nodes
        odd_nodes = {}
        while len(queue) > 0:
            node, level = queue.pop()
            # print(node, level)
            if level % 2 == 1:
                if level not in odd_nodes: odd_nodes[level] = []
                odd_nodes[level].append(node)
            if node.left is not None:
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))

        for level, nodes in odd_nodes.items():
            self.reverseNodes(nodes)

        return root

    def reverseNodes(self, nodes: List[int]) -> None:
        vals = [node.val for node in nodes]
        # print(vals)
        reversed_vals = list(reversed(vals))
        for i in range(len(nodes)):
            node = nodes[i]
            node.val = reversed_vals[i]

