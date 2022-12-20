class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a_count = {}
        b_count = {}
        for a in A.split():
            if a in a_count:
                a_count[a] += 1
            else:
                a_count[a] = 1
        for b in B.split():
            if b in b_count:
                b_count[b] += 1
            else:
                b_count[b] = 1

        uncommon = []
        for counted_a in a_count:
            if a_count[counted_a] < 2 and counted_a not in b_count:
                uncommon.append(counted_a)
        for counted_b in b_count:
            if b_count[counted_b] < 2 and counted_b not in a_count:
                uncommon.append(counted_b)
        return uncommon
        