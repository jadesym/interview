class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        front = 0
        back = len(s) - 1
        while front < back:
            first = s[front].lower()
            last = s[back].lower()
            if not first.isalnum():
                front += 1
            elif not last.isalnum():
                back -= 1
            elif first != last: return False
            else:
                front += 1
                back -= 1
        return True
        