from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        if len(traversal) == 0: return None
        # key: level
        # value: latest node at level
        node_stack = {}
        level, num, curIndex = self.getNext(traversal, 0)
        root = TreeNode(num)
        node_stack[level] = root
        while curIndex < len(traversal):
            nextLevel, nextNum, nextIndex = self.getNext(traversal, curIndex)
            newNode = TreeNode(nextNum)
            prevLevelNode = node_stack[nextLevel - 1]

            if prevLevelNode.left is None:
                prevLevelNode.left = newNode
            else:
                prevLevelNode.right = newNode
            
            node_stack[nextLevel] = newNode

            curIndex = nextIndex

        return root

    # (level, number, newIndex)
    def getNext(self, traversal: str, index: int) -> tuple[int, int, int]:
        curIndex = index
        level = 0
        digits = []
        while traversal[curIndex] == '-':
            level += 1
            curIndex += 1
        while curIndex < len(traversal) and traversal[curIndex] != '-':
            digits.append(int(traversal[curIndex]))
            curIndex += 1
        return (level, self.getNum(digits), curIndex)
    def getNum(self, digits: List[int]) -> int:
        curNum = 0
        for digit in digits:
            curNum *= 10
            curNum += digit
        return curNum