class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxDepth = 0
        for char in s:
            if char == "(":
                depth += 1
                if depth > maxDepth:
                    maxDepth = depth
            elif char == ")":
                depth -= 1
            else:
                pass
        return maxDepth