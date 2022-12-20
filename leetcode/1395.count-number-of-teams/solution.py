class Solution:
    def numTeams(self, rating: List[int]) -> int:
        forwardMapping = {}
        for i in range(len(rating) - 1):
            forwardMapping[i] = []
            for j in range(i, len(rating)):
                if rating[i] > rating[j]:
                    forwardMapping[i].append(j)
        backwardMapping = {}
        for i in range(len(rating) - 1):
            backwardMapping[i] = []
            for j in range(i, len(rating)):
                if rating[i] < rating[j]:
                    backwardMapping[i].append(j)

        forwardMappingCount = 0
        for firstIndex, secondIndices in forwardMapping.items():
            for secondIndex in secondIndices:
                if secondIndex in forwardMapping:
                    forwardMappingCount += len(forwardMapping[secondIndex])
        backwardMappingCount = 0
        for firstIndex, secondIndices in backwardMapping.items():
            for secondIndex in secondIndices:
                if secondIndex in backwardMapping:
                    backwardMappingCount += len(backwardMapping[secondIndex])
        return forwardMappingCount + backwardMappingCount
