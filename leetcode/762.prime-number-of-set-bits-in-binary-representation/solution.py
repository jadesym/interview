class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        all_primes = {2, 3, 5, 7, 11, 13, 17, 19}
        prime_bits_count = 0
        for num in range(L, R+1):
            if self.getOnes(num) in all_primes: prime_bits_count += 1
        return prime_bits_count

    def getPrimes(self, high):
        all_primes = []
        for val in range(2, high + 1):
            if self.isPrime(val, all_primes): all_primes.add(val)
        return all_primes
        
    def isPrime(self, count, primes_so_far):
        if count >= 2:
            for divisor in primes_so_far:
                if divisor > (count // 2): break
                if count % divisor == 0:
                    return False
            return True
        else:
            return False
    def getOnes(self, num):
        count = 0
        num_copy = num
        while num_copy > 0:
            count += num_copy & 1
            num_copy >>= 1
        return count
        