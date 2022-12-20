class Solution:
    def countAsterisks(self, s: str) -> int:
        in_pair = False
        count = 0
        for char in s:
            if not in_pair and char == "|":
                in_pair = True
            elif in_pair and char == "|":
                in_pair = False
            elif char == "*" and not in_pair:
                count += 1
        return count
        