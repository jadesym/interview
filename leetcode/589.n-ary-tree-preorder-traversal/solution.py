from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root):
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
            for child_index in range(len(curNode.children) - 1, -1, -1):
                queue.append(curNode.children[child_index])
        return array
