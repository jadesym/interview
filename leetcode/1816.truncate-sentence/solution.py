class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        result = ""
        word_count = 0
        for char in s:
            if char == " ":
                word_count += 1
            if word_count == k:
                break
            result += char
        return result