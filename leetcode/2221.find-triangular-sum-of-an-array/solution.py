class Solution:
    # 1: 1
    # 2: 1, 1
    # 3: 1, 2, 1
    # 4: 1, 3, 3, 1
    # 5: 1, 4, 6, 4, 1
    # 6: 1, 5, 10, 5, 1
    def triangularSum(self, nums: List[int]) -> int:
        curNums = nums
        while len(curNums) > 1:
            newNums = [0] * (len(curNums) - 1)
            for i in range(len(newNums)):
                newNums[i] = (curNums[i] + curNums[i + 1]) % 10
            curNums = newNums
        return curNums[0]