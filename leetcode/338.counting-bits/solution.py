class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0: return [0]
        array = [0]*(num+1)
        array[1] = 1
        curExponent = 1
        for x in range(2, num + 1):
            if 2 ** (curExponent + 1) == x:
                curExponent += 1
                array[x] = 1
            else:
                array[x] = array[x-2**curExponent] + 1
        return array
            