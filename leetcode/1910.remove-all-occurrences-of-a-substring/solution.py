class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for char in s:
            stack.append(char)
            self.removeIfOccurrence(stack, part)
        return "".join(stack)
    def removeIfOccurrence(self, stack: List[str], part: str) -> None:
        if len(stack) < len(part): return
        stackIndex = len(stack) - 1
        isMatch = True
        for i in range(len(part) - 1, -1, -1):
            partChar = part[i]
            if stack[stackIndex] != partChar:
                isMatch = False
                break
            stackIndex -= 1
        if isMatch:
            for i in range(len(part)):
                stack.pop()
        return