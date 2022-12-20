class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xors = []
        xors.append(nums[0])
        max_num = self.getMaxNum(maximumBit)
        for i in range(1, len(nums)):
            xors.append(xors[len(xors) - 1] ^ nums[i])
        result = []
        for i in range(len(xors) - 1, -1, -1):
            val = xors[i]
            result.append(max_num ^ val)
        return result
    def getMaxNum(self, maximumBit: int):
        num = 1
        for i in range(1, maximumBit):
            num *= 2
            num += 1
        return num