class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner_set = set()
        loser_set = set()
        single_loss_set = set()
        for winner, loser in matches:
            if loser in loser_set:
                if loser in single_loss_set:
                    single_loss_set.remove(loser)
            else:
                single_loss_set.add(loser)

            winner_set.add(winner)
            loser_set.add(loser)


        return [sorted(list(winner_set.difference(loser_set))), sorted(list(single_loss_set))]