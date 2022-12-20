class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        height = len(nums)
        first_row = nums[0]
        width = len(first_row)

        if r * c != height * width: return nums
        
        newRowIndex = 0
        newColIndex = 0
        newArray = []
        newCurRow = []
        for oldRowIndex in range(height):
            for oldColIndex in range(width):
                newCurRow.append(nums[oldRowIndex][oldColIndex])
                # print(newCurRow)
                if len(newCurRow) == c:
                    newArray.append(newCurRow)
                    newCurRow = []
        return newArray
