class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        num_count = set()

        for a in A:
            if a in num_count:
                return a
            else:
                num_count.add(a)
        raise Exception()
        