class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        one_found = False
        counter = 0
        max_counter = 0
        n_copy = N
        while n_copy > 0:
            if n_copy % 2 == 0:
                if one_found: counter += 1
            else:
                if one_found:
                    max_counter = max(max_counter, counter + 1)
                counter = 0
                one_found = True
            n_copy //= 2
        return max_counter
                
        