import sys

class WordDistanceFinder:
    """
    This class will be given a list of words (such as might be tokenized
    from a paragraph of text), and will provide a method that takes two
    words and returns the shortest distance (in words) between those two
    words in the provided text. For example, in this paragraph if your
    first string was "words" and your second string was "the", your program
    should return 2. If you were given "given" and the word "were", you
    should return 1.
    """
    def __init__(self, words):
        # Implementation here
         self.lookup = {}
         for index in range(len(words)):
             word = words[index]
             if word in self.lookup: self.lookup[word].append(index)
             else: self.lookup[word] = [index]
    def distance(self, wordOne, wordTwo):
        # Implementation here
        try:
            oneIndices = self.lookup[wordOne]
            twoIndices = self.lookup[wordTwo]
            if wordOne == wordTwo:
                return 0
            else:
                return self.indexDistance(oneIndices, twoIndices)
        except:
            return -1
    def indexDistance(self, oneIndices, twoIndices):
        i, j = 0, 0
        minDist = sys.maxsize
        while i < len(oneIndices) and j < len(twoIndices):
            oneIndex = oneIndices[i]
            twoIndex = twoIndices[j]
            minDist = min(abs(oneIndex - twoIndex), minDist)
            if oneIndex >= twoIndex:
                j += 1
            else:
                i += 1
        return minDist

tests = {
    ("the", "quick", "brown", "fox", "quick", 'jumps'): {
        ("fox", "the"): 3,
        ("quick", "fox"): 1,
        ("fox", "fox"): 0,
        ("x", "fox"): -1,
        ("fox", "x"): -1,
        ("a", "b"): -1,
        ("quick", "brown"): 1,
        ("the", "jumps"): 5
    }
}

for initialSet in tests:
    wdf = WordDistanceFinder(initialSet)
    test_cases = tests[initialSet]
    for test_case in test_cases:
        print(test_case, test_cases[test_case])
        assert wdf.distance(test_case[0], test_case[1]) == test_cases[test_case]
