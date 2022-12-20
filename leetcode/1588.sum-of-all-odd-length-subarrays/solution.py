class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        subarrayLengths = [i + 1 for i in range(0, len(arr), 2)]
        countAtIndex = {}
        for index in range(len(arr)):
            for subarrayLength in subarrayLengths:
                lowerBoundForIndex = 0 if (index + 1 - subarrayLength) < 0 else index + 1 - subarrayLength
                upperBoundForIndex = len(arr) - 1 if (index - 1 + subarrayLength) >= len(arr) else index - 1 + subarrayLength
                
                boundDifference = upperBoundForIndex - lowerBoundForIndex
                numInstances = boundDifference - subarrayLength + 2
                # print(arr[index], subarrayLength, numInstances)
                if index in countAtIndex: countAtIndex[index] += numInstances
                else: countAtIndex[index] = numInstances
        sumResult = 0
        for index in range(len(arr)):
            element = arr[index]
            sumResult += element * countAtIndex[index]
        return sumResult
