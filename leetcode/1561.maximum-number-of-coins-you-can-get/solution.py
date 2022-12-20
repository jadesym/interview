class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles = sorted(piles)
        # print(sorted_piles)
        num_piles_per = len(sorted_piles) // 3
        max_coins = 0
        for i in range(1, num_piles_per + 1):
            index = len(sorted_piles) - 2 * i
            max_coins += sorted_piles[index]
            # print(index, sorted_piles[index])

        return max_coins
