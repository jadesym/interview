class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []
        for char in s:
            if len(stack) == 0:
                if char not in mapping.keys(): return False
                stack.append(char)
            else:
                cur = stack[len(stack) - 1]
                if mapping[cur] != char: 
                    if char in mapping.keys():
                        stack.append(char)
                    else:
                        return False
                else: stack.pop()
        if len(stack) != 0: return False
        return True