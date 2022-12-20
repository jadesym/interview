# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        queue = deque([(root, 0)])
        curLevel = 0
        result = []
        curResult = []
        while len(queue) > 0:
            cur, level = queue.popleft()
            if level > curLevel:
                result.append(curResult)
                curResult = [cur.val]
                curLevel = level
            else: 
                curResult.append(cur.val)
            if cur.left is not None:
                queue.append((cur.left, level + 1))
            if cur.right is not None:
                queue.append((cur.right, level + 1))
        if len(curResult) > 0: result.append(curResult)
        return result