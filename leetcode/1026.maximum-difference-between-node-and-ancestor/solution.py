# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)[0]

    # (maxDiff, min, max)
    def dfs(self, node: TreeNode) -> tuple[Optional[int], int, int]:
        if node.left is None and node.right is None:
            return (None, node.val, node.val)

        curVal = node.val

        leftTuple = None if node.left is None else self.dfs(node.left)
        rightTuple = None if node.right is None else self.dfs(node.right)

        leftMaxDiff = None if leftTuple is None else leftTuple[0]
        rightMaxDiff = None if rightTuple is None else rightTuple[0]
        maxDiff = self.getMost(leftMaxDiff, rightMaxDiff, True)

        leftMin = None if leftTuple is None else leftTuple[1]
        rightMin = None if rightTuple is None else rightTuple[1]
        minVal = self.getMost(leftMin, rightMin, False)

        leftMax = None if leftTuple is None else leftTuple[2]
        rightMax = None if rightTuple is None else rightTuple[2]
        maxVal = self.getMost(leftMax, rightMax, True)

        newMaxDiff = max(abs(curVal - minVal), abs(curVal - maxVal)) if maxDiff is None else max(abs(curVal - minVal), abs(curVal - maxVal), maxDiff)
        newMaxVal = max(maxVal, curVal)
        newMinVal = min(minVal, curVal)
        return (newMaxDiff, newMinVal, newMaxVal)

    def getMost(self, leftVal: Optional[int], rightVal: Optional[int], isMax: bool):
        if leftVal is None and rightVal is None:
            return None
        elif leftVal is None:
            return rightVal
        elif rightVal is None:
            return leftVal
        else:
            if isMax:
                return max(leftVal, rightVal)
            else:
                return min(leftVal, rightVal)
