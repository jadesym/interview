class Solution:
    def fairCandySwap(self, A: 'List[int]', B: 'List[int]') -> 'List[int]':
        aSum = sum(A)
        bSum = sum(B)
        bSet = set(B)
        
        diff = aSum - bSum
        for a in A:
            expectedB = a - diff // 2
            if expectedB in bSet:
                return [a, expectedB]
        return None