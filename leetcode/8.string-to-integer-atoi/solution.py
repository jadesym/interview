class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        status = {
            's':{' ':'s', '+':'p', '-':'p', 'd':'d', 'o':'e'},
            'p':{' ':'e', '+':'e', '-':'e', 'd':'d', 'o':'e'},
            'd':{' ':'e', '+':'e', '-':'e', 'd':'d', 'o':'e'},
            'e':{' ':'e', '+':'e', '-':'e', 'd':'e', 'o':'e'}
        }
        s = 's'
        pos = 1
        ret = 0
        flag = True
        for each in str:
            if each in '1234567890':
                token = 'd'
            elif each in ' +-':
                token = each
            else:
                token = 'o'
            s = status[s][token]
            if s == 's':
                continue
            elif s == 'p':
                pos = each == '+' and 1 or -1
            elif s == 'd':
                ret = ret * 10 + ord(each) - ord('0')
            else:
                return self.fil(ret, pos)
        return self.fil(ret, pos)
        
    def fil(self, num, pos):
        if num >> 31 != 0:
            return pos == 1 and 2147483647 or -2147483648
        return pos * num