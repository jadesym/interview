class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors = [arr[0]] * len(arr)
        for i in range(1, len(arr)):
            xors[i] = xors[i - 1] ^ arr[i]

        results = [None] * len(queries)
        for i in range(len(queries)):
            start, end = queries[i]
            if start == 0:
                results[i] = xors[end]
            else:
                results[i] = xors[end] ^ xors[start - 1]
        return results