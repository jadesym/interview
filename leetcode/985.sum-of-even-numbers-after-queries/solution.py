class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        result = []
        evens = sum([a for a in A if a % 2 == 0])
        for query in queries:
            val, index = query
            old_val = A[index]
            A[index] += val
            new_val = A[index]
            if old_val % 2 == 0 and new_val % 2 == 0:
                evens += new_val - old_val
            elif old_val % 2 == 0:
                evens -= old_val
            elif new_val % 2 == 0:
                evens += new_val
            else: pass
            result.append(evens)
            
            
        return result