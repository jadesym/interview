class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        result = []
        for i in range(len(s)):
            curX, curY = startPos
            numActions = 0
            for j in range(i, len(s)):
                instruction = s[j]
                if instruction =="R":
                    curY += 1
                elif instruction == "D":
                    curX += 1
                elif instruction == "L":
                    curY -= 1
                elif instruction == "U":
                    curX -= 1
                if curY < 0 or curY >= n:
                    break
                if curX < 0 or curX >= n:
                    break
                numActions += 1
            result.append(numActions)
        return result
            