from functools import cmp_to_key

class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        letter_weights = {letter: index for index, letter in enumerate(order)}
        for index in range(len(words) - 1):
            first_word = words[index]
            second_word = words[index + 1]
            if self.compare_words(first_word, second_word, letter_weights) > 0: return False
        return True
        
    def compare_words(self, first, second, letter_weights):
        first_len = len(first)
        second_len = len(second)
        index = 0
        while index < first_len or index < second_len:
            if index >= first_len: return -1
            elif index >= second_len: return 1
            first_letter = first[index]
            second_letter = second[index]
            if letter_weights[first_letter] < letter_weights[second_letter]: return -1
            elif letter_weights[first_letter] > letter_weights[second_letter]: return 1
            index += 1
        return 0