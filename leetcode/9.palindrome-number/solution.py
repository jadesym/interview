class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        front = 0
        back = len(string) - 1
        while front < back:
            if string[front] != string[back]:
                return False
            front += 1
            back -=1
        return True