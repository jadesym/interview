class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        end_index = None
        for i in range(len(word)):
            if word[i] == ch:
                end_index = i
                break
        if end_index is None: return word
        result = [None] * len(word)
        for j in range(end_index // 2 + 1):
            result[j] = word[end_index - j]
            result[end_index - j] = word[j]
            # print(result)
        for i in range(end_index + 1, len(word)):
            result[i] = word[i]
            # print(result)
        # print(result)
        return "".join(result)
