class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        numToIndex = {}
        for index in range(len(numbers)):
            num = numbers[index]
            if num in numToIndex:
                numToIndex[num].append(index)
            else:
                numToIndex[num] = [index]
        for val in numToIndex:
            if val == target - val:
                return [numToIndex[val][0] + 1, numToIndex[val][1] + 1]
            elif target - val in numToIndex:
                valIndex = numToIndex[val][0]
                targetIndex = numToIndex[target-val][0]
                return [min(valIndex, targetIndex) + 1, max(valIndex, targetIndex) + 1]