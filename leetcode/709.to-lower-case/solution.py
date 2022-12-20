class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return ''.join([a.lower() for a in str])