class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            match = True
            # print(word)
            lookup = {}
            reverse_lookup = {}
            for i in range(len(word)):
                wordChar = word[i]
                patternChar = pattern[i]
                if patternChar not in lookup:
                    lookup[patternChar] = wordChar
                elif lookup[patternChar] != wordChar:
                    match = False
                    break

                if wordChar not in reverse_lookup:
                    reverse_lookup[wordChar] = patternChar
                elif reverse_lookup[wordChar] != patternChar:
                    match = False
                    break

                # print(wordChar, patternChar, lookup)

            if match:
                result.append(word)


        return result