class Solution:
    def minFlips(self, target: str) -> int:
        if len(target) == 0: return 0

        numContiguous = 0
        prevChar = None

        for char in target:
            if prevChar is None and char == '1':
                numContiguous += 1
            if prevChar is not None and char != prevChar:
                numContiguous += 1
            prevChar = char

        return numContiguous
        