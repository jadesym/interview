class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        lastNum = None
        isIncreasing = None
        for num in nums:
            if lastNum is None:
                lastNum = num
                continue
            if isIncreasing is None:
                if num > lastNum:
                    isIncreasing = True
                elif num < lastNum:
                    isIncreasing = False
            else:
                if num > lastNum and isIncreasing == False:
                    return False
                if num < lastNum and isIncreasing == True:
                    return False
            lastNum = num
        return True
        