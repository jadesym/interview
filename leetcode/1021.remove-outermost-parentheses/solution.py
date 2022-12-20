class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        openParensCount = 0
        new_str = ""
        for char in s:
            if char == "(":
                if openParensCount >= 1:
                    new_str += char
                openParensCount += 1
            elif char == ")":
                if openParensCount > 1:
                    new_str += char
                openParensCount -= 1

        return new_str