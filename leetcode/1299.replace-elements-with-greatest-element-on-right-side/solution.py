class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxes = [0] * len(arr)
        maxes[len(arr) - 1] = arr[len(arr) - 1]
        for i in range(len(arr) - 2, -1, -1):
            maxes[i] = max(maxes[i + 1], arr[i])
        result = [-1] * len(maxes)
        for i in range(1, len(maxes)):
            result[i - 1] = maxes[i]
        return result

