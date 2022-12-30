class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr, key=lambda num: (self.getBits(num), num))
        return sorted_arr
    def getBits(self, num: int) -> int:
        oneBits = 0
        curNum = num
        while curNum > 0:
            oneBits += curNum % 2
            curNum //= 2
        return oneBits