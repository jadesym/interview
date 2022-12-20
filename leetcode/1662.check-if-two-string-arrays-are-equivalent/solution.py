class Solution:
    def getNextIndices(self, wordIndex: int, characterIndex: int, words: List[str]) -> [int, int]:
        if wordIndex >= len(words):
            return [None, None]
        if characterIndex >= len(words[wordIndex]) - 1:
            if wordIndex < len(words) - 1:
                return [wordIndex + 1, 0]
            else:
                return [None, None]
        else:
            return [wordIndex, characterIndex + 1]

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if len(word1) == 0 and len(word2) == 0:
            return True

        word1WordIndex = 0
        word1CharacterIndex = 0
        word2WordIndex = 0
        word2CharacterIndex = 0

        while word1WordIndex is not None and word2WordIndex is not None:
            if word1[word1WordIndex][word1CharacterIndex] != word2[word2WordIndex][word2CharacterIndex]:
                return False

            word1WordIndex, word1CharacterIndex = self.getNextIndices(word1WordIndex, word1CharacterIndex, word1)
            word2WordIndex, word2CharacterIndex = self.getNextIndices(word2WordIndex, word2CharacterIndex, word2)

        if word1WordIndex is None and word2WordIndex is None:
            return True
        else:
            return False