class Solution(object):
    def calcArea(self, i, j, k, l):
        return (k - i) * (l - j)
    
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        first = self.calcArea(A, B, C, D)
        second = self.calcArea(E, F, G, H)
        width = 0
        height = 0
        if A < E:
            if C > E:
                width = min(G, C) - E
            else:
                pass
        else:
            if G > A:
                width = min(G, C) - A 
            else:
                pass
        if D < H:
            if F < D:
                height = D - max(B, F)
            else:
                pass
        else:
            if B < H:
                height = H - max(B, F)
            else:
                pass
        print(first, second, width, height, width * height)
        return first + second - width * height
            
                
        
        