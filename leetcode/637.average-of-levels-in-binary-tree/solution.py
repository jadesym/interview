from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        currentLevel = 0
        currentLevelArrays = {}
        queue = deque([(0, root)])
        while len(queue) > 0:
            level, node = queue.popleft()
            if node is None: continue
            if level == currentLevel:
                if level in currentLevelArrays:
                    currentLevelArrays[level].append(node.val)
                else:
                    currentLevelArrays[level] = [node.val]
            else:
                currentLevelArrays[level] = [node.val]
                currentLevel = level
            queue.append((level + 1, node.left))
            queue.append((level + 1, node.right))
        result = []
        for given_level in range(currentLevel + 1):
            level_array = currentLevelArrays[given_level]
            result.append(sum(level_array) / len(level_array))
        return result