class Solution:
    def sortString(self, s: str) -> str:
        s_set = set(list(s))
        sorted_chars = sorted(list(s_set))
        remaining_chars = {}
        for char in s:
            if char not in remaining_chars:
                remaining_chars[char] = 0
            remaining_chars[char] += 1

        result = ""
        index = None
        forward = True
        while len(result) < len(s):
            newIndex, newForward = self.getNextIndex(remaining_chars, sorted_chars, index, forward)
            newChar = sorted_chars[newIndex]
            remaining_chars[newChar] -= 1
            result += newChar
            index, forward = newIndex, newForward
        return result
    def getNextIndex(self, remaining_chars: Dict[str, int], sorted_chars: List[str], curIndex: Optional[int] = None, isForward: bool = True) -> tuple[int, bool]:
        if curIndex == None: return (0, True)

        newIndex = curIndex
        newIsForward = isForward

        if isForward == True:
            newIndex += 1
        else:
            newIndex -= 1
        
        while newIndex >= len(sorted_chars) or newIndex < 0 or remaining_chars[sorted_chars[newIndex]] <= 0:
            if newIndex == len(sorted_chars):
                newIsForward = False
                newIndex -= 1
            elif newIndex < 0:
                newIsForward = True
                newIndex += 1
            elif remaining_chars[sorted_chars[newIndex]] <= 0:
                if newIsForward:
                    newIndex += 1
                else:
                    newIndex -= 1
        return (newIndex, newIsForward)


