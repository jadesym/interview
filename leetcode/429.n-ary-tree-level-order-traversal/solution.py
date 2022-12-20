from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        traversal = []
        currentLevel = 0
        currentLevelArray = []
        queue = deque([(0, root)])
        while len(queue) > 0:
            item = queue.popleft()
            level, node = item[0], item[1]
            if node is None: continue
            if level == currentLevel:
                currentLevelArray.append(node.val)
            else:
                traversal.append(currentLevelArray)
                currentLevelArray = [node.val]
                currentLevel = level
            for child in node.children:
                queue.append((level + 1, child))
        if len(currentLevelArray) > 0:
            traversal.append(currentLevelArray)
        return traversal