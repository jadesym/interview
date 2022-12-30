# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        parent_set = set()
        child_set = set()

        # key: parent
        # value: {left: val, right, val}
        edges = {}

        for parent, child, isLeft in descriptions:
            parent_set.add(parent)
            child_set.add(child)
            if parent not in edges: edges[parent] = {
                'left': None,
                'right': None
            }
            if isLeft == 1:
                edges[parent]['left'] = child
            else:
                edges[parent]['right'] = child

        rootVal = list(parent_set.difference(child_set))[0]
        rootNode = TreeNode(rootVal)

        queue = [rootNode]
        while len(queue) > 0:
            curNode = queue.pop()
            curVal = curNode.val

            if curVal not in edges:
                continue

            node_edges = edges[curVal]
            leftVal = node_edges['left']
            rightVal = node_edges['right']

            if leftVal is not None:
                newLeftNode = TreeNode(leftVal)
                curNode.left = newLeftNode
                queue.append(newLeftNode)
            if rightVal is not None:
                newRightNode = TreeNode(rightVal)
                curNode.right = newRightNode
                queue.append(newRightNode)

        return rootNode