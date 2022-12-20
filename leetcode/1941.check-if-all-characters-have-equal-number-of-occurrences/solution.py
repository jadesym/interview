class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occurrences = {}
        for char in s:
            if char not in occurrences:
                occurrences[char] = 0
            occurrences[char] += 1
        valToMatch = None
        for key, val in occurrences.items():
            if valToMatch is None:
                valToMatch = val
            elif val != valToMatch:
                return False
        return True