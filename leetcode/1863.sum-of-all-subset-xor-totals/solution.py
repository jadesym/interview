class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsetXORsMaps = [{} for i in range(len(nums))]
        for i in range(len(nums)):
            num = nums[i]
            curMap = subsetXORsMaps[i]

            if i > 0:
                prevXORMap = subsetXORsMaps[i - 1]
                for prevXOR, count in prevXORMap.items():
                    newIncludingXOR = prevXOR ^ num
                    newExcludingXOR = prevXOR
                    self.insertXOR(curMap, newIncludingXOR, count)
                    self.insertXOR(curMap, newExcludingXOR, count)
            self.insertXOR(curMap, num)

        
        total = 0

        for val, count in subsetXORsMaps[len(nums) - 1].items():
            total += val * count

        # for elem in subsetXORsMaps:
        #     print(elem)
        return total

    def insertXOR(self, xorMap: Dict[int, int], val: int, count: int = 1):
        if val in xorMap:
            xorMap[val] += count
        else:
            xorMap[val] = count

