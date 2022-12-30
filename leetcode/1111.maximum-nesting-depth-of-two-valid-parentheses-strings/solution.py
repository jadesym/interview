class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        if len(seq) == 0: return []
        level = 0
        max_level = -1
        char_level = [None] * len(seq)

        for i in range(len(seq)):
            char = seq[i]
            if char == '(':
                level+=1
            max_level = max(max_level, level)
            char_level[i] = level
            if char == ')':
                level -= 1
            # print(char, char_level)
        b_level = max_level // 2
        a_level = max_level - b_level

        # print(char_level)
        # print(a_level, b_level)
        result = [None] * len(seq)
        for i in range(len(char_level)):
            char_height = char_level[i]

            if char_height <= a_level:
                result[i] = 1
            else:
                result[i] = 0
        return result
            

        