from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        array = []
        queue = deque([root])
        while len(queue) > 0:
            curNode = queue.pop()
            if curNode is None: continue
            array.append(curNode.val)
            for child in curNode.children:
                queue.append(child)
        array.reverse()
        return array

    # def dfs(self, root, array):
    #     if root is None: return
    #     for child in root.children:
    #         self.dfs(child, array)
    #     array.append(root.val)