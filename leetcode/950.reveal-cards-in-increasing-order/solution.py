from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorted_deck = sorted(deck)
        cards = deque()
        for i in range(len(sorted_deck) - 1, -1, -1):
            cards.rotate(1)
            cards.appendleft(sorted_deck[i])
        return list(cards)