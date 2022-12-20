class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if len(A) < 1:
            return 0
        word_length = len(A[0])
        indices_to_delete = 0
        for word_index in range(0, word_length):
            last_char = None
            for a in A:
                if last_char is None:
                    last_char = a[word_index]
                elif a[word_index] < last_char:
                    indices_to_delete += 1
                    break
                else:
                    last_char = a[word_index]
        return indices_to_delete
                