class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        descendingBoxTypes = sorted(boxTypes, key=lambda box: box[1], reverse=True)
        curSize = 0
        index = 0
        unitCount = 0
        while curSize < truckSize and index < len(boxTypes):
            remaining = truckSize - curSize
            sizeAtGivenType = descendingBoxTypes[index][0]
            sizeAdded = min(remaining, sizeAtGivenType)
            curSize += sizeAdded
            unitCount += descendingBoxTypes[index][1] * sizeAdded

            index += 1
        return unitCount