class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        fixed = 0
        parensStack = 0
        for char in s:
            if char == "(":
                parensStack += 1
            else:
                parensStack -= 1
            if parensStack < 0:
                fixed += 1
                parensStack += 1
        return fixed + parensStack

