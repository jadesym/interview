class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        charSets = []
        self.dfs(characters, 0, combinationLength, [], charSets)
        self.character_sets = ["".join(charSet) for charSet in charSets]
        self.curIndex = 0

    def next(self) -> str:
        combination = self.character_sets[self.curIndex]
        self.curIndex += 1
        return combination

    def hasNext(self) -> bool:
        return self.curIndex < len(self.character_sets)

    def dfs(self, characters: str, index: int, combinationLength: int, charSoFar: List[str], charSet: List[List[str]]) -> None:
        if len(charSoFar) == combinationLength:
            charSet.append(charSoFar)
            return

        if index >= len(characters):
            return

        curChar = characters[index]

        self.dfs(characters, index + 1, combinationLength, charSoFar + [curChar], charSet)
        self.dfs(characters, index + 1, combinationLength, charSoFar, charSet)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()