class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        last_bit = None
        n_copy = n
        while n_copy > 0:
            current_bit = n_copy & 1
            if last_bit is None:
                last_bit = current_bit
            elif last_bit == current_bit:
                return False
            last_bit = current_bit
            n_copy >>= 1

        return True