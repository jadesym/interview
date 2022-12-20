from collections import defaultdict

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        itemWeightArray = [0] * 1001
        for val, weight in items1 + items2:
            itemWeightArray[val] += weight

        result = []
        for val in range(len(itemWeightArray)):
            weight = itemWeightArray[val]
            if weight > 0:
                result.append([val, weight])
        return result