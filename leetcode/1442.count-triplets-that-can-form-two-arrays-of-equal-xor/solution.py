class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        xors = [None] * len(arr)
        xors[0] = arr[0]

        xorsToIndices = {0: [-1]}
        for i in range(len(arr)):
            newXor = None
            if i == 0:
                newXor = arr[0]
            else:
                newXor = xors[i - 1] ^ arr[i]
            xors[i] = newXor
            if newXor not in xorsToIndices: xorsToIndices[newXor] = []
            xorsToIndices[newXor].append(i)
        
        # print(xors)
        # print(xorsToIndices)

        total_counts = 0
        for xorVal, indices in xorsToIndices.items():
            total_counts += self.getComboCounts(indices)

        return total_counts
    def getComboCounts(self, indices: List[int]) -> int:
        if len(indices) == 1: return 0
        count = 0
        for i in range(len(indices) - 1):
            for j in range(i + 1, len(indices)):
                iIndex = indices[i]
                jIndex = indices[j]
                count += jIndex - iIndex - 1
        return count

