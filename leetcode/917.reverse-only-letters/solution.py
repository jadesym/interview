from string import ascii_letters

class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        result = list(S)
        letters = set(list(ascii_letters))
        low_index = 0
        high_index = len(S) - 1
        while low_index < high_index:
            low = S[low_index]
            high = S[high_index]
            if low not in letters:
                low_index += 1
                continue
            if high not in letters:
                high_index -= 1
                continue
            result[low_index], result[high_index] = result[high_index], result[low_index]
            low_index += 1
            high_index -= 1
        return "".join(result)
            
        