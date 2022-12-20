

class Solution:
    def __init__(self):
        lower_chars = string.ascii_lowercase
        self.lower_chars = lower_chars
        self.char_map = {}
        for i in range(len(lower_chars)):
            self.char_map[lower_chars[i]] = i
        self.num_chars = len(lower_chars)

    def replaceDigits(self, s: str) -> str:
        new_str = ""
        last_char = None
        for char in s:
            if char in self.char_map:
                new_str += char
                last_char = char
            else:
                shift = int(char)
                cur_index = self.char_map[last_char]
                new_index = (cur_index + shift) % self.num_chars
                new_char = self.lower_chars[new_index]
                new_str += new_char
        return new_str