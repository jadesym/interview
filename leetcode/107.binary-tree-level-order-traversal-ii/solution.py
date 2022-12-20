# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        return self.bfs(root)
    def bfs(self, root):
        levelDict = {}
        queue = deque([(root, 0)])
        maxLevel = 0
        while len(queue) > 0:
            current, level = queue.popleft()
            if level > maxLevel:
                maxLevel = level
            if level in levelDict:
                levelDict[level].append(current.val)
            else:
                levelDict[level] = [current.val]
            if current.left is not None:
                queue.append((current.left, level + 1))
            if current.right is not None:
                queue.append((current.right, level + 1))
        sol = []
        for level in range(maxLevel, -1, -1):
            sol.append(levelDict[level])
        return sol
        
        