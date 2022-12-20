class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0: return 0
        elif N == 1: return 1
        sequence = [0] * (N + 1)
        sequence[1] = 1
        for index in range(2, N + 1):
            sequence[index] = sequence[index - 2] + sequence[index - 1]
        return sequence[N]