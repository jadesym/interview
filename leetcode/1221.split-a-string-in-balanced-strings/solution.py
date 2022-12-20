class Solution:
    def balancedStringSplit(self, s: str) -> int:
        splitCount = 0
        lCount = 0
        rCount = 0
        for char in s:
            if char == "R":
                rCount += 1
            elif char == "L":
                lCount += 1
            else:
                pass

            if lCount != 0 and rCount != 0 and lCount == rCount:
                splitCount += 1
                lCount = 0
                rCount = 0
            
        return splitCount