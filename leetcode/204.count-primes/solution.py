class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 0
        if n == 3: return 1
        already = [False]*(n)
        count = 1
        for num in range(3, n, 2):
            cur = num
            if already[cur]: continue
            count += 1
            while cur < n:
                already[cur] = True
                cur += num
        return count