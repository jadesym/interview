import math

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = math.floor(math.log(label, 2))
        remainder = label - 2 ** level
        realLabel = label if level % 2 == 0 else 2 ** level + (2 ** level - remainder - 1)
        # print(level, realLabel)
        curLabel = realLabel
        curLevel = level

        result = [0] * (level + 1)
        while curLabel > 0:
            if curLevel % 2 == 1:
                result[curLevel] = (3 * (2 ** curLevel) - curLabel - 1)
            else:
                result[curLevel] = curLabel
            curLabel //= 2
            curLevel -= 1

        return result