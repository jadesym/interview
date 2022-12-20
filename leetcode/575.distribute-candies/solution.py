class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candy_set = set(candies)
        return min(len(candy_set), len(candies) // 2)
        