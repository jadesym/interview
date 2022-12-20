class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        array = [start + 2 * i for i in range(n)]
        xor = array[0]
        for i in range(1, len(array)):
            xor ^= array[i]
        return xor